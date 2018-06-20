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

if __name__ == '__main__':
    count = 0
    # redis 连接
    my_rds = rds()
    # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
    redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT
    while(True):
        count += 1
        print(count)
        data1 = my_rds.blpop_data(REDIS_KAFKA_LIST)
        data1 = data1.decode()
        data2 = my_rds.SetGetHashData(REDIS_KAFKA_HASHSET,data1)
        print(data1)
        print(data2)
        time.sleep(1)
        # sendtowx(returndata)
