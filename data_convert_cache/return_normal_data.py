#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

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
    # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
    redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT
    while(True):
        returndata = my_rds.blpop_data(redis_list_compute_result)
        returndata = json.loads(returndata.decode())
        logger.info(str(returndata))
        # sendtowx(returndata)
