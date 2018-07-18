#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import time

# local
from data_convert_cache.util_redis import Redis_db as rds
from data_convert_cache.data_convert_catche_func import *
from data_convert_cache.util_log import *

# online
# from util_redis import Redis_db as rds
# from data_convert_catche_func import *
# from util_log import *

# 日志获取
logger = get_logger(LOG_FILE_PATH_RETURN_ABNORMAL, "return-abnormal-data-log")

# Redis连接并初始化
my_rds = rds()

# 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT
count = 0
while(True):
    try:
        # 记录开始时间
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 从redis中读取计算完的脚型数据，并返回到接口
        returndata = my_rds.blpop_data(redis_list_compute_result)

        if returndata != False:
            returndata = json.loads(returndata.decode())

            # 记录中间时间
            middle_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # sendtowx(returndata)

            # 记录结束时间
            end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(count)
            count += 1
            # 日志输出
            logger.info('[' + str(returndata) + '],' + '[data read from redis and send to port],'  + '[' + middle_time + '],' + '[' + start_time + '],' + '[' + end_time + ']')
    except Exception as e:
        logger.error(str(e))
