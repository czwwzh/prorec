#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# # dev_env
# consume earliest available messages, don't commit offsets
from kafka import KafkaConsumer

consumer = KafkaConsumer('footInfoTest',
                         group_id='my-group2',
                         bootstrap_servers=['52.80.96.173:9092', '52.80.129.73:9092', '52.80.147.244:9092'])

for message in consumer:
    print(message.key)
    print(type(message.value))
    print(message.value)
