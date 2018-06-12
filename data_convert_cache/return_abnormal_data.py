#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# local
from data_convert_cache.configuration import *
from data_convert_cache.util_redis import Redis_db as rds
from data_convert_cache.data_convert_catche_func import *
from data_convert_cache.util_log import logger

# online
# from configuration import *
# from util_redis import Redis_db as rds
# from data_convert_catche_func import *
# from util_log import logger

if __name__ == '__main__':
    # redis 连接
    my_rds = rds()
    # etl 异常数据 uuid 存储队列
    redis_list_footdata_except = REDIS_LIST_FOOTDATA_EXCEPT
    while(True):
        uuid = my_rds.blpop_data(redis_list_footdata_except)
        uuid = uuid.decode()
        returndata = {'uuid': uuid, 'res': -1}
        # sendtowx(returndata)
        logger.info(str(returndata))
