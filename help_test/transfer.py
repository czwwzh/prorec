#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from kafka import KafkaConsumer

from model.local.modelv1.dataetl.redisutil import Redis_db as rds

consumer = KafkaConsumer('footInfoProd',
                         group_id='my-group21',
                         bootstrap_servers=['54.222.152.174:9092', '54.222.195.114:9092', '52.80.73.74:9092'])
my_rds = rds('recommend_data_msg')
for message in consumer:
    my_rds.RpushData(message)

    # key = message.key
    # value = message.value
    # print(key)
    # print(value)

