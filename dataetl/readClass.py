#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# local
# from dataetl.etl_func import *
# from dataetl.util_log import logger

# online
from etl_func import *
from util_log import logger


class readClass:
    def __init__(self):
        pass

    def StartRun(self,uuid):
        logger.info('0.redis connect and get data start time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # redis 连接
        my_rds = rds()

        # redis 队列  哈希表定义
        # redis 哈希表中存储的源数据 uuid  footdata
        redis_kafka_hashset = REDIS_KAFKA_HASHSET
        # etl 异常数据 uuid 存储队列
        redis_list_footdata_except = REDIS_LIST_FOOTDATA_EXCEPT
        # etl 正常数据 uuid 存储队列
        redis_list_foot_etl = REDIS_LIST_FOOT_ETL


        # 取数据
        ist = True
        try:
            # 从redis 源数据哈希表中读取脚数据
            foot_data = my_rds.SetGetHashData(redis_kafka_hashset, uuid)
            foot_data = foot_data.decode()
            logger.info(uuid)
            logger.info('1.data from redis_hashset time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        except:
            ist = False

        if ist == False:
            my_rds.rpush_data(redis_list_footdata_except,uuid)
            return

        # 源脚数据入库
        # sourcedata save
        res = foot_data_save_mysql(uuid, foot_data)

        # data dataetl
        if res > 0:
            logger.info('2.data save to mysql time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # filter data which is not str type
            res1 = stream_str(uuid, foot_data)
            logger.info('3.filter data which is not str type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # 异常脚入redis 队列
            if res1 == False:
                my_rds.rpush_data(redis_list_footdata_except, uuid)
                return

            # filter data which is not json type
            res2 = stream_json(uuid, foot_data)
            logger.info('4.filter data which is not json type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # 异常脚入redis 队列
            if res2 == False:
                my_rds.rpush_data(redis_list_footdata_except, uuid)
                return

            # 将源字符串格式脚数据转为json对象
            # transform data to json
            foot_data = json.loads(foot_data)
            logger.info('5.transform data to json time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            # 过滤异常脚数据
            # filter abnormal foot data
            res3 = footfilter(uuid, foot_data)
            logger.info('6.filter abnormal foot data time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # 异常脚入redis 队列
            if res3 == False:
                my_rds.rpush_data(redis_list_footdata_except, uuid)
                return

            # 脚数据解析
            # get foot data in demend
            foot_data = get_foot_data(foot_data)
            logger.info('7.get foot data in demend time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            # etl 之后的脚放入redis队列
            try:
              foot_data = json.dumps(foot_data)
              my_rds.rpush_data(redis_list_foot_etl, foot_data)
              logger.info(uuid + '--->success,send to redis etl ')
              logger.info('8.foot etl send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
            except Exception as e:
                logger.info(str(e))
        else:
            try:
                my_rds.rpush_data(redis_list_footdata_except, uuid)
                repetive_data_save(uuid, foot_data)
            except Exception as e:
                logger.info(str(e))


