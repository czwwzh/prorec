#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
from kafka import KafkaConsumer, KafkaProducer
# from time import sleep
# import pymysql
import time
from projecttest.kafkaprocon.foot1 import *
from projecttest.kafkaprocon.foot2 import *
from projecttest.kafkaprocon.foot3 import *
from projecttest.kafkaprocon.foot4 import *

from projecttest.kafkaprocon.uuid1 import *
from projecttest.kafkaprocon.uuid2 import *
from projecttest.kafkaprocon.uuid3 import *
from projecttest.kafkaprocon.uuid4 import *

uuid1.extend(uuid2)
uuid1.extend(uuid3)
uuid1.extend(uuid4)
foot1.extend(foot2)
foot1.extend(foot3)
foot1.extend(foot4)
print(len(uuid1))
print(len(foot1))
if __name__ == '__main__':
    #
    # producer_resend = KafkaProducer(
    #                          bootstrap_servers=['54.222.152.174:9092' , '54.222.195.114:9092', '52.80.73.74:9092'])

    producer = KafkaProducer(
        bootstrap_servers=['54.222.152.174:9092', '54.222.195.114:9092', '52.80.73.74:9092'])
    # uuidlist = uui
    # footdatalist = footdata
    # for i in range(1000):
    #     uuid = uuidlist[i]
    #     print(uuid)
    #     value = footdatalist[i]
    #     print(value)

    # print(len(footdata1))
    # print(len(uuiddata1))



    print('1.start time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                time.localtime()))
    for i in range(10):
        print(i)
        uuid = uuid1[i]
        value = foot1[i]
        # print(uuid)
        # print(value)
        producer.send('footcom', key=uuid.encode('utf-8'), value=value.encode('utf-8'))
        time.sleep(0.05)
        # if i % 100 == 0:
        #     time.sleep(1)
    print('2.end time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                time.localtime()))





