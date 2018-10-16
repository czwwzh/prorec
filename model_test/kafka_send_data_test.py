#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time
from kafka import KafkaProducer

from func import *
from uuid__shop_no import *


def get_foot_data(uuid_tuple):
    import pymysql

    db = None
    cursor = None


    sql = "select data from " + FOOT_SCAN_TABLE + " where uuid in" + str(uuid_tuple)


    result = None
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        result = cursor.fetchall()

    except Exception as e:
        logger.info(str(e))
        logger.info("save foot_scan exception")
    finally:
        if cursor != None:
            # 关闭游标
            cursor.close()
        if db != None:
            # 关闭数据库连接
            db.close()
    return result


producer = KafkaProducer(
        bootstrap_servers=['10.240.12.26:9092','10.240.251.129:9092','10.240.251.130:9092'])



foot_data_list = get_foot_data(tuple(uuid))
count = 0
for i in range(len(foot_data_list)):
    foot_data = json.loads(foot_data_list[i][0])
    uuid = foot_data['UUID']
    foot_data = json.dumps(foot_data)
    print(count)
    print(uuid)
    print(foot_data)
    count += 1
    producer.send('epoque_bigdata_footInfoprod', key=uuid.encode('utf-8'), value=foot_data.encode('utf-8'))
    time.sleep(2)


