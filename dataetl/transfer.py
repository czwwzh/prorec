#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time

from kafka import KafkaConsumer
from redisutil import Redis_db as rds
from logutil import logger
from dataetlconfiguration import *
consumer = KafkaConsumer(KAFKA_PROD_FOOTTOPIC,
                         group_id=KAFKA_GROUP_ID,
                         bootstrap_servers=KAFKA_PROD_BROKERS)
my_rds = rds('recommend_data_msg')
for message in consumer:
    try:
        logger.info('data from kafka to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        key = message.key.decode()
        sourcedata = message.value.decode()
        my_rds.SetData(key,sourcedata)
        my_rds.RpushData(key)
        logger.info(key)
    except:
        pass

