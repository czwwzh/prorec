#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# # dev_env
# consume earliest available messages, don't commit offsets
from kafka import KafkaConsumer
import time
consumer = KafkaConsumer('footInfoProd',
                         group_id='my-group13',
                         bootstrap_servers=['54.222.152.174:9092', '54.222.195.114:9092', '52.80.73.74:9092'])

count = 0
for message in consumer:
    count += 1
    print(count)
    print('kafkaprocon consumer time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                   time.localtime()))
    print(message.key)
    #print(type(message.value))
    print(message.value)
