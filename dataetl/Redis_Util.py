#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import redis
import time

# local
# from dataetl.etl_configuration_test import *
# from dataetl.Log_Util import Logger


# online
from etl_configuration_prod import *
from Log_Util import Logger

# 获取日志实例
logger = Logger("data-etl-log-1",LOG_FILE_PATH,0).getLogger()




class Redis_db:

    # redis 配置 连接 及队列定义
    redis_info = REDIS_CONNECT_INFO
    redis_conn = None

    # redis队列初始化,连接redis
    def __init__(self):
        self.link_redis()

    # redis 链接  失败再连接三次 一次隔1S
    def link_redis(self,num = 0):
        conf = self.redis_info

        logger.info('start connect redis')

        self.redis_conn = redis.Redis(**conf)

        try:
            self.redis_conn.ping()
            logger.info('connect redis ---> Success!')
            return True
        except redis.exceptions.ConnectionError as e:
            logger.info("connect redis ---> Failed!")
            logger.error(str(e))
            time.sleep(1)
            num += 1
            if num < 3:
                self.link_redis(num)
            return False

    # 向redis 队列中放入数据
    # 从队列的右边入队一个元素 rpush
    # 参数：数据 对列名
    def rpush_data(self, redis_list, data):
        try:
            self.redis_conn.ping()
            self.redis_conn.rpush(redis_list, data)
        except redis.exceptions.ResponseError:
            logger.info("ping redis failed!")
        except Exception as e:
            logger.info("Rpush data to redis failed!")
            logger.error(str(e))

    # 从redis 队列中读取数据，一次读取完队列中的数据
    # 删除并获得该列表中的第一元素，或阻塞，直到有一个可用 blpop
    # 参数：队列名
    def blpop_data(self,redis_list):
        try:
            self.redis_conn.ping()
            # 返回队列名和数据
            if self.redis_conn.exists(redis_list):
                _,json = self.redis_conn.blpop(redis_list,timeout = 1)
                return json
            else:
                return False
        except redis.exceptions.ResponseError:
            logger.info("ping redis failed!")
        except Exception as e:
            logger.info("Blpop data from redis failed!")
            logger.error(str(e))
            return False

    # 获取队列长度
    # 参数： 队列名
    def len_redis_list(self,redis_list):
        len_list = 0
        # 链接是否异常
        try:
            self.redis_conn.ping()
            len_list = self.redis_conn.llen(redis_list)
        except redis.exceptions.ResponseError:
            logger.info("ping redis failed!")
        except Exception as e:
            logger.info("get len(redis_list) failed!")
            logger.error(str(e))
        return len_list

    # 向redis哈希表中存取数据
    # 参数 哈希表名  uuid  数据
    def SetGetHashData(self, hash_set, uuid, data=None):
        res = False
        # 链接是否异常
        try:
            self.redis_conn.ping()
            # 数据不为空，则添加数据
            if data != None:
                self.redis_conn.hset(hash_set, uuid, data)
            # 数据为空
            else:
                res = self.redis_conn.hget(hash_set, uuid)
            return res
        except redis.exceptions.ResponseError:
            logger.info("ping redis failed!")
        except Exception as e:
            logger.info("hset or hget hash_set failed!")
            logger.error(str(e))


