#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import pymysql
import time

# local
from data_compute.util_log import logger
from data_compute.compute_configuration import *
from data_compute.util_redis import Redis_db as rds
from data_compute.variables import *


# online
# from util_log import logger
# from compute_configuration import *
# from util_redis import Redis_db as rds
# from variables import *


# 取脚长度（左右脚最大值）上下五个码
def get_sizes(foot_length_left,foot_length_right):

    sizes = []
    if foot_length_left > foot_length_right:
        foot_length = foot_length_left
    else:
        foot_length = foot_length_right
    sizes = sizes + [foot_length - 10, foot_length - 5, foot_length, foot_length + 5, foot_length + 10]
    for size in sizes:
        if size < 200 or size > 300:
            sizes.remove(size)
    return sizes

# last data dataetl ============================================
# 获取当前门店商品的主要两个季
def get_year_sean(shop_no):
    year = None
    season = None
    flag = True
    try:
        my_rds = rds()
        year = time.strftime('%Y', time.localtime(time.time()))
        year = year[3]
        season = my_rds.SetGetHashData(REDIS_HASHSET_SHOP_SEASON,shop_no)
        season = tuple(season.decode().split(','))
    except Exception as e:
        flag = False
        logger.info("get year season failed")
        logger.info(str(e))
    return (year, season, flag)


# 获取相应门店相应楦数据
# get last data
def get_last_data(shop_no,sex, sizes):
    lastlist = []
    sex = str(sex)
    year_quarter = get_year_sean(shop_no)
    if year_quarter[2] == False:
        return lastlist

    sql = "SELECT " + LASTATTRIBUTESSTR + " FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + sex + " and year = '" + str(
        year_quarter[0]) + "' and season in " + str(year_quarter[1]) + " and  basicsize in " + str(sizes)

    db = None
    cursor = None

    try:
        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for last in result:
            lasts = get_last_data_value(last)
            lastlist.append(lasts)
    except Exception as e:
        logger.info("no last data to fecth ")
        logger.info(str(e))
    finally:
        if  cursor != None:
            cursor.close()
        if  db != None:
            db.close()
    return lastlist

# 将数据库中查询的单条楦数据放到集合中
# transfer last data sql result to dict
def get_last_data_value(data):
    lastdata = dict()
    index = 0
    for lastfield in LASTATTRIBUTES:
        lastdata[lastfield] = data[index]
        index = index + 1
    return lastdata



# 楦查询和脚楦合并
# foot and last data connect
# get last data by shopno and foot join last
def foot_connect_last(data):
    #  取脚长度（左右脚最大值）上下五个码
    sizes = get_sizes(data['foot_length_left'],data['foot_length_right'])

    shop_no = data['shop_no']
    sex = data['customer_sex']

    # 获取门店相应楦数据
    last_list = get_last_data(shop_no,sex,tuple(sizes))
    footlasts = list()
    if last_list != []:
        # 脚楦连接
        for shop_last in last_list:
            footlasts.append(dict(data,**shop_last))
    return footlasts



# 按指定书序获取size模型计算所需要的数据和用户信息
# get left data right data alone for suit data_compute
# return [[uuid,algoversion,shop_no,shoelastbaseno,basicsize,sex,left,right]]
def get_etl_data_left_right_alone(data):
    leftrightdatas = list()
    for leftrightdata in data:
        uuid = leftrightdata['UUID']
        algoversion = leftrightdata['algoVersion']
        shop_no = leftrightdata['shop_no']
        shoelastbaseno = leftrightdata['shoelastbaseno']
        basicsize = leftrightdata['basicsize']
        sex = leftrightdata['customer_sex']

        left = list()
        right = list()

        for field in FOOT_LAST_ORDER_LEFT_DIMENSIONS:
            left.append(leftrightdata[field])

        for field in FOOT_LAST_ORDER_RIGHT_DIMENSIONS:
            right.append(leftrightdata[field])
        leftrightdatas.append([uuid,algoversion,shop_no,shoelastbaseno,basicsize,sex,left,right])
    return leftrightdatas


# 按指定顺序获取舒适度模型计算所需要的数据和用户信息
# get left  right data together for size data_compute
# return [[uuid, algoversion, shop_no, shoelastbaseno, basicsize, sex, leftright]]
def get_etl_data_left_right_together(data):
    leftrightdatas = list()
    for leftrightdata in data:
        uuid = leftrightdata['UUID']
        algoversion = leftrightdata['algoVersion']
        shop_no = leftrightdata['shop_no']
        shoelastbaseno = leftrightdata['shoelastbaseno']
        basicsize = leftrightdata['basicsize']
        sex = leftrightdata['customer_sex']

        leftright = list()

        for field in FOOT_LAST_ORDER_DIMENSIONS:
            leftright.append(leftrightdata[field])
        leftrightdatas.append([uuid, algoversion, shop_no, shoelastbaseno, basicsize, sex, leftright])
    return leftrightdatas

# 模型计算结果处理
# result process
# return dict(key:list(dict)})
def result_data_process(data):
    resultdict = dict()
    for result in data:
        if result[0] in resultdict:
            resultdict[result[0]].append(result[1])
        else:
            resultlist = list()
            resultlist.append(result[1])
            resultdict[result[0]] = resultlist
    return resultdict


# 所有模型计算结果存储
# result save
def result_save_batch(result_list):
    import happybase
    import time
    # model data_compute time
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        connection = happybase.Connection(host=HBASE_HOST, port=HBASE_PORT, timeout=HBASE_TIMEOUT, protocol=HBASE_PROTOCOL,
                                          transport=HBASE_TRANSPORT)
        table = connection.table(HBASE_RESULT_TABLE)
        # 批量插入连接
        b = table.batch(timestamp=int(time.time()))
        # 遍历模型与模型版本名
        for (data,modelversion) in result_list:
            # 模型计算结果更新时间定义
            updatetimename = modelversion + '_' + "updatetime"
            # 遍历耽搁模型计算结果
            for result in data:
                # result
                datasave = json.dumps(data[result])

                res = result.split("_")
                # rowkey uuid_algoVersion
                uuid_version = res[0] + '_' + res[1]
                # shoelastbaseno
                shoelastbaseno = res[2]
                # sex
                sex = res[3]
                # column family : column
                columns1 = "user_info:sex"
                columns2 = "user_info:" + updatetimename
                columns3 = modelversion + ':' + shoelastbaseno

                b.put(uuid_version, {columns1: sex,
                                     columns2: updatetime,
                                     columns3: datasave})
        b.send()
        connection.close()
    except Exception as e:
        logger.info(str(e))
        logger.info("save data_compute result exception!")
