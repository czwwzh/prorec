#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from kafka import KafkaConsumer
from redisutil import Redis_db as rds

from dataetlconfiguration import *
consumer = KafkaConsumer(KAFKA_PROD_FOOTTOPIC,
                         group_id=KAFKA_GROUP_ID,
                         bootstrap_servers=KAFKA_PROD_BROKERS)
my_rds = rds('recommend_data_msg')
for message in consumer:
    try:
        key = message.key.decode()
        sourcedata = message.value.decode()
        # data = key + "_" + sourcedata
        my_rds.SetData(key,sourcedata)
        my_rds.RpushData(key)
        print(key)
    except:
        pass

