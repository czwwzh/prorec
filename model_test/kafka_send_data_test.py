#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time
from kafka import KafkaProducer

# 预处理所用库配置
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_CHARSET = 'utf8mb4'
# 线上表
# online
RECOMMEND_DB_NAME = 'shop_sku_recommend'
FOOT_SCAN_TABLE = 'foot_scan'
FOOT_REPEAT_TABLE = 'foot_repeat'

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
        print("ssss")
    finally:
        if cursor != None:
            # 关闭游标
            cursor.close()
        if db != None:
            # 关闭数据库连接
            db.close()
    return result




uuid = ["YB20180804180033USUkHKijVYmLseDI","YB20180803133459SEvJRWxB7lDH2bax","YB20170706150402txxEfxu0BYe0C92r","YB20170810161026FOOzTxYlfpzVjst1",
"TX20180606201407ALLFa431U44JzHj2",
"TX20180606204016qhLLXKV7bMCTbtSl",
"TX20180606212542pM1W5LeSUT34bBeC",
"TX20180607100428sm43LPNZIa6ev5dO"]

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


