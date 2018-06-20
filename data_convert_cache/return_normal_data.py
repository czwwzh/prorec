#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time

# local
# from data_convert_cache.util_redis import Redis_db as rds
# from data_convert_cache.data_convert_catche_func import *
# from data_convert_cache.util_log import *

# online
from util_redis import Redis_db as rds
from data_convert_catche_func import *
from util_log import *

if __name__ == '__main__':
    # 日志获取
    logger = get_logger(LOG_FILE_PATH_RETURN_NORMAL, "return-normal-data-log")
    # redis 连接
    my_rds = rds()
    # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
    redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT
    count = 0
    while(True):
        count += 1
        logger.info(count)
        returndata = my_rds.blpop_data(redis_list_compute_result)
        returndata = json.loads(returndata.decode())
        logger.info(str(returndata))
        # time.sleep(1)
        sendtowx(returndata)
