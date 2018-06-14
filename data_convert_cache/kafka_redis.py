#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
from kafka import KafkaConsumer

# local
from data_convert_cache.util_redis import Redis_db as rds
from data_convert_cache.util_log import logger
from data_convert_cache.configuration import *

# online
# from redisutil import Redis_db as rds
# from logutil import logger
# from configuration import *


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
        logger.info('data from kafka to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        # kafka源数据解码
        key = message.key.decode()
        sourcedata = message.value.decode()
        # uuid 和 value 放入redis的哈希表中
        redis_con.SetGetHashData(redis_hashset,key,sourcedata)
        # uuid 放入 redis 的队列中
        redis_con.rpush_data(redis_list,key)

        logger.info(key)
    except:
        pass


