#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# local
from data_convert_cache.util_redis import Redis_db as rds
from data_convert_cache.util_redis import *
from data_convert_cache.data_convert_catche_func import *



# 日志获取
logger = get_logger(LOG_FILE_PATH_RETURN_ABNORMAL, "return-abnormal-data-log")
# redis 连接
my_rds = rds()
# etl 异常数据 uuid 存储队列
redis_list_footdata_except = REDIS_LIST_FOOTDATA_EXCEPT
count = 0
while (True):
    try:
        # 记录开始时间
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 从redis中读取过滤掉的脚型数据，并返回到接口
        uuid = my_rds.blpop_data(redis_list_footdata_except)
        if uuid != False:
            uuid = uuid.decode()
            returndata = {'uuid': uuid, 'res': -1}

            # 记录中间时间
            middle_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # sendtowx(returndata)

            # 记录结束时间
            end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logger.info(count)
            count += 1
            # 日志输出
            logger.info('[' + uuid + '],' + '[data read from redis and send to port],' + '[' + str(
                returndata) + '],' + '[' + middle_time + '],' + '[' + start_time + '],' + '[' + end_time + ']')
    except Exception as e:
        logger.error(str(e))



