#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time
from kafka import KafkaProducer

# 2.预处理所用库配置
RECOMMEND_DB_HOST = '10.240.18.136'
RECOMMEND_DB_PORT = 3306
RECOMMEND_DB_CHARSET = 'utf8mb4'
RECOMMEND_DB_USER = "root"
RECOMMEND_DB_PASSWORD = "epoque123"
RECOMMEND_DB_NAME = 'epoque_rds'
FOOT_SCAN_TABLE = 'foot_scan'
FOOT_REPEAT_TABLE = 'foot_repeat'

def get_foot_data(uuid_tuple):
    import pymysql

    db = None
    cursor = None


    sql = "select data from " + FOOT_SCAN_TABLE + " where uuid in" + str(uuid_tuple)


    result = list()
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        result = cursor.fetchall()

    except Exception as e:
        print("ssss")
    finally:
        if cursor != None:
            # 关闭游标
            cursor.close()
        if db != None:
            # 关闭数据库连接
            db.close()
    return result




uuid = ["TX20170527161228f8ZjtoSfmy3aF3ny",
"TX20170612090630CB1rZWIIDus8xMO2",
"TX20180206164247atsZub6gqeuUU3XT",
"TX20180207142158MxIGpbFBS60eua0d",
"TX20180210065400IPVIOgywrGBHUkSt",
"TX20180210065537D4UvNiVPUMZSItxV",
"TX20180210112541oSNMskXGJPGOwapW",
"TX20180210140326I9Clx29LjWRRQALx",
"TX201802101514002Qg99UeNUxk6ZilX",
"TX20180210151724JTBGtLplhLFItQJH"]

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
    time.sleep(1)


