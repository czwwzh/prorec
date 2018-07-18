#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
from kafka import KafkaConsumer

# local
from data_convert_cache.util_redis import Redis_db as rds
from data_convert_cache.util_log import *
from data_convert_cache.configuration import *

# online
# from util_redis import Redis_db as rds
# from util_log import *
# from configuration import *

# 日志获取
logger = get_logger(LOG_FILE_PATH_KAFKA_REDIS,"kafka-redis-log")
# kafka连接
consumer = KafkaConsumer(KAFKA_PROD_FOOTTOPIC,
                         group_id=KAFKA_GROUP_ID,
                         bootstrap_servers=KAFKA_PROD_BROKERS)
# 初始化redis
redis_con = rds()

# redis 队列和HashMap定义
redis_list = REDIS_KAFKA_LIST
redis_hashset = REDIS_KAFKA_HASHSET

# 从kafka中读取数据
for message in consumer:
    try:
        # 记录开始时间
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 读取kafka数据放入redis中
        # kafka源数据解码
        key = message.key.decode()
        sourcedata = message.value.decode()
        # uuid 和 value 放入redis的哈希表中
        redis_con.SetGetHashData(redis_hashset,key,sourcedata)
        # uuid 放入 redis 的队列中
        redis_con.rpush_data(redis_list,key)

        # 记录结束时间
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 打印日志
        logger.info('[' + key + '],' + '[data from kafka to redis],' + '[' + start_time + '],' + '[' + end_time + ']')
    except Exception as e:
        logger.error(str(e))



