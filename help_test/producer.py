#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
consumer = KafkaConsumer('footInfoTest',
                         group_id='my-group',
                         bootstrap_servers=['52.80.96.173:9092', '52.80.129.73:9092', '52.80.147.244:9092'])

producer_resend = KafkaProducer(
                         client_id='footInfoSoftTest-Group',
                         bootstrap_servers=['52.80.96.173:9092', '52.80.129.73:9092', '52.80.147.244:9092'])


i = 1
for message in consumer:
    i = i + 1
    producer_resend.send('footInfoTest', key=message.key,value=message.value)
    if i % 5 == 0:
        sleep(5)
