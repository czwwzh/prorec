#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time
from kafka import KafkaProducer

from model_test.func import *
from model_test.util_log import *
from model_test.uuid__shop_no import *

# 日志获取
logger = get_logger(LOG_FILE_PATH,"send-foot-data-log")


producer = KafkaProducer(
        bootstrap_servers=['54.222.152.174:9092', '54.222.195.114:9092', '52.80.73.74:9092'])


foot_data_list = get_foot_data(tuple(uuid))

# 固定门店号
# count = 0
# for (scanId,shop_no) in scan_id_shop_no:
#     # print(scanId)
#     # print(shop_no)
#     for i in range(len(foot_data_list)):
#         foot_data = json.loads(foot_data_list[i][0])
#
#         uuid = foot_data['UUID'] + '_' + shop_no
#         foot_data['scanId'] = scanId
#         foot_data['UUID'] = uuid
#
#         foot_data = json.dumps(foot_data)
#         print(count)
#         print(uuid)
#         print(foot_data)
#         count += 1
#
#         producer.send('footcom', key=uuid.encode('utf-8'), value=foot_data.encode('utf-8'))
#         # time.sleep(0.05)
#         time.sleep(1)


count = 0
for i in range(len(foot_data_list)):
    foot_data = json.loads(foot_data_list[i][0])
    uuid = foot_data['UUID']
    foot_data = json.dumps(foot_data)
    print(count)
    print(uuid)
    print(foot_data)
    count += 1
    producer.send('footcom', key=uuid.encode('utf-8'), value=foot_data.encode('utf-8'))
    # time.sleep(0.05)
    time.sleep(5)


