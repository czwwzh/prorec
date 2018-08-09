#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers = ['52.80.73.74:9092'])

producer = KafkaProducer(
                         bootstrap_servers=['54.222.152.174:9092' , '54.222.195.114:9092', '52.80.73.74:9092'])

# Assign a topic
topic = 'compute'

def test():
    print('begin')
    n = 1
    aaa = 'hello zhanhao'
    while(n <= 3):
        producer.send(topic,key="uuuuu".encode("utf-8"), value=aaa.encode("utf-8"))
        print("send" + str(n))
        n += 1
        time.sleep(0.5)
    print('done')


if __name__ == '__main__':
    test()