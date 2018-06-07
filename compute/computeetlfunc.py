#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import pymysql
from computeconfiguration import *
from variables import *

from logutil import logger


#import traceback

# get status and judge it is not 0
def statusexist(uuid):
    ist = 0
    sql = "SELECT status FROM " + FOOT_LAST_ETL_TABLE + " where uuid = '" + uuid + "' limit 1"
    db = None
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist is None:
            ist = 0
    except:
        # print("Error: unable to fecth status")
        logger.info("Error: unable to fecth status")

    finally:
            if db:
                db.close()
    return ist

# get foot and last data by uuid return list[dict]
def getetldata(uuid):
    footlastlist = list()
    sql = "SELECT " + FOOT_LAST_ORDER_DIMENSIONSSTR + " FROM " + FOOT_LAST_ETL_TABLE + " where uuid = '" + uuid + "'"
    db = None
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist == 0 or ist == None:
            updateexceptioncode(uuid,-4)
            return None
        results = cursor.fetchall()
        for result in results:
            footlast = getFootLastData(result)
            footlastlist.append(footlast)
    except:
        # print("Error:fecth foot and last data exception by uuid")
        logger.info("Error:fecth foot and last data exception by uuid")
    finally:
        if db:
            db.close()
    return footlastlist

# get one foot and last return a dict
def getFootLastData(data):
    footlastdata = dict()
    index = 7
    for field in FOOT_LAST_ORDER_DIMENSIONS:
        footlastdata[field] = data[index]
        index = index + 1

    footlastdata['uuid'] = data[1],
    if type(footlastdata['uuid']) == tuple:
        footlastdata['uuid'] = footlastdata['uuid'][0]

    footlastdata['algoversion'] = data[2],
    if type(footlastdata['algoversion']) == tuple:
        footlastdata['algoversion'] = footlastdata['algoversion'][0]

    footlastdata['shop_no'] = data[3],
    if type(footlastdata['shop_no']) == tuple:
        footlastdata['shop_no'] = footlastdata['shop_no'][0]

    footlastdata['styleno'] =  data[4],
    if type(footlastdata['styleno']) == tuple:
        footlastdata['styleno'] = footlastdata['styleno'][0]

    footlastdata['basicsize'] = data[5]
    footlastdata['sex'] = data[6]

    return footlastdata

# get left data right data alone for suit compute
# return [[uuid,algoversion,shop_no,styleno,basicsize,sex,left,right]]
def getetldataleftrightalone(data):
    leftrightdatas = list()
    for leftrightdata in data:
        uuid = leftrightdata['uuid']
        algoversion = leftrightdata['algoversion']
        shop_no = leftrightdata['shop_no']
        styleno = leftrightdata['styleno']
        basicsize = leftrightdata['basicsize']
        sex = leftrightdata['sex']

        left = list()
        right = list()

        for field in FOOT_LAST_ORDER_LEFT_DIMENSIONS:
            left.append(leftrightdata[field])

        for field in FOOT_LAST_ORDER_RIGHT_DIMENSIONS:
            right.append(leftrightdata[field])
        leftrightdatas.append([uuid,algoversion,shop_no,styleno,basicsize,sex,left,right])
    return leftrightdatas

# get left  right data together for size compute
# return [[uuid, algoversion, shop_no, styleno, basicsize, sex, leftright]]
def getetldataleftrighttogether(data):
    leftrightdatas = list()
    for leftrightdata in data:
        uuid = leftrightdata['uuid']
        algoversion = leftrightdata['algoversion']
        shop_no = leftrightdata['shop_no']
        styleno = leftrightdata['styleno']
        basicsize = leftrightdata['basicsize']
        sex = leftrightdata['sex']

        leftright = list()

        for field in FOOT_LAST_ORDER_DIMENSIONS:
            leftright.append(leftrightdata[field])
        leftrightdatas.append([uuid, algoversion, shop_no, styleno, basicsize, sex, leftright])
    return leftrightdatas


# result process
# return dict(key:list(dict)})
def resultdataprocess(data):
    resultdict = dict()
    for result in data:
        if result[0] in resultdict:
            resultdict[result[0]].append(result[1])
        else:
            resultlist = list()
            resultlist.append(result[1])
            resultdict[result[0]] = resultlist
    return resultdict

# # result save
# def resultsave(data,modelversion):
#     import happybase
#     import time
#     ip = HBASE_HOST
#     connection = happybase.Connection(host=ip, port=HBASE_PORT, timeout=HBASE_TIMEOUT, protocol=HBASE_PROTOCOL,
#                                       transport=HBASE_TRANSPORT)
#     table = connection.table(HBASE_RESULT_TABLE)
#     # model compute time
#     updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     updatetimename = modelversion + '_' + "updatetime"
#     for result in data:
#         # result
#         datasave = json.dumps(data[result])
#
#         res = result.split("_")
#         # rowkey uuid_algoVersion
#         uuid_version = res[0] + '_' + res[1]
#         # styleno
#         styleno = res[2]
#         # sex
#         sex = res[3]
#         # column family : column
#         columns1 = "user_info:sex"
#         columns2 = "user_info:" + updatetimename
#         columns3 = modelversion + ':' + styleno
#
#         table.put(uuid_version, {columns1: sex,
#                            columns2: updatetime,
#                            columns3: datasave})
#     connection.close()

# result save
def resultsave(data,modelversion):
    # data = result[0]
    # modelversion = result[1]
    import happybase
    import time
    ip = HBASE_HOST
    connection = None
    try:
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
            # styleno
            styleno = res[2]
            # sex
            sex = res[3]
            # column family : column
            columns1 = "user_info:sex"
            columns2 = "user_info:" + updatetimename
            columns3 = modelversion + ':' + styleno

            b.put(uuid_version, {columns1: sex,
                               columns2: updatetime,
                               columns3: datasave})
        b.send()
    except Exception as e:
        logger.info(e)
    finally:
        if connection != None:
            connection.close()


def updateexceptioncode(uuid,exceptioncode):

    import pymysql

    db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                         user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                         db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
    cursor = db.cursor()
    sql = "update " + FOOT_SCAN_TABLE +  " set exceptioncode = " + str(exceptioncode) + " where uuid = '" + uuid +"'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # print("updateexceptioncode exception")
        logger.info("updateexceptioncode exception")
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

