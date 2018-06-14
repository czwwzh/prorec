#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import pymysql

# local
from compute.util_log import logger
from compute.compute_configuration import *


# online
# from util_log import logger
# from compute_configuration import *



# 按指定书序获取size模型计算所需要的数据和用户信息
# get left data right data alone for suit compute
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
# get left  right data together for size compute
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

# 模型计算结果存储
# result save
def result_save(data, modelversion):
    import happybase
    import time
    ip = HBASE_HOST
    connection = happybase.Connection(host=ip, port=HBASE_PORT, timeout=HBASE_TIMEOUT, protocol=HBASE_PROTOCOL,
                                      transport=HBASE_TRANSPORT)
    table = connection.table(HBASE_RESULT_TABLE)
    # model compute time
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    updatetimename = modelversion + '_' + "updatetime"
    b = table.batch(timestamp=int(time.time()))


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

# 所有模型计算结果存储
# result save
def result_save_batch(result_list):
    import happybase
    import time
    # model compute time
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
        logger.info("save compute result exception!")
