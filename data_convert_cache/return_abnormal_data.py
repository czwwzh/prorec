#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time

# local
# from data_convert_cache.util_redis import Redis_db as rds
# from data_convert_cache.data_convert_catche_func import *

# online
from util_redis import Redis_db as rds
from data_convert_catche_func import *

if __name__ == '__main__':
    # 日志获取
    logger = get_logger(LOG_FILE_PATH_RETURN_ABNORMAL, "return-abnormal-data-log")
    # redis 连接
    my_rds = rds()
    # etl 异常数据 uuid 存储队列
    redis_list_footdata_except = REDIS_LIST_FOOTDATA_EXCEPT
    while(True):
        uuid = my_rds.blpop_data(redis_list_footdata_except)
        uuid = uuid.decode()
        returndata = {'uuid': uuid, 'res': -1}
        sendtowx(returndata)
        logger.info(str(returndata))
        # time.sleep(1)

