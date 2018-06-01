#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json

import pymysql
import time

from dataetlconfiguration import *
from logutil import logger

# import traceback


# foot data dataetl ============================================
# sourcedata save
def footdatasavemysql(uuid,footdata):
    import time
    import pymysql
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                         user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                         db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
    cursor = db.cursor()
    value = (uuid,footdata,updatetime)
    sql = "INSERT IGNORE INTO " + FOOT_SCAN_TABLE + " (uuid,data,updatetime) "+ " VALUES "  + str(value)
    ist = 0
    try:
        # 执行sql语句
        ist = cursor.execute(sql)
        if ist is None:
            ist = 0
        # 执行sql语句
        db.commit()
    # except Exception as e:
    except:
        # print("save foot_scan exception")
        logger.info("save foot_scan exception")

        # traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    return ist

# updateexceptioncode for table foot_scan
# def updateexceptioncode(uuid,exceptioncode):
#     import pymysql
#     db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
#                          user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
#                          db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
#     cursor = db.cursor()
#     sql = "update " + FOOT_SCAN_TABLE +  " set exceptioncode = " + str(exceptioncode) + " where uuid = '" + uuid +"'"
#     print(sql)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 执行sql语句
#         db.commit()
#     except:
#         print("updateexceptioncode exception")
#         # 如果发生错误则回滚
#         db.rollback()
#     # 关闭游标
#     cursor.close()
#     # 关闭数据库连接
#     db.close()

# exception data save mysql
def exceptiondataupdate(comment,uuid,exceptiontype):
    import pymysql
    db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                         user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                         db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
    cursor = db.cursor()
    sql = "update " + FOOT_SCAN_TABLE +  " set exceptiontype = " + str(exceptiontype) + ", comment = '" + comment + "' where uuid = '" + uuid +"'"
    # print(sql)
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


# # exception data save hbase
# def exceptiondata( data, comment, UUID,exceptiontype):
#     import happybase
#     import time
#     connection = happybase.Connection(host=HBASE_HOST, port=HBASE_PORT, timeout=HBASE_TIMEOUT, protocol=HBASE_PROTOCOL,
#                                       transport=HBASE_TRANSPORT)
#     table = connection.table(HBASE_EXCEPTION_TABLE)
#     time = str(int(time.time()))
#     if UUID == None:
#         UUID = time
#     table.put(UUID, {"extra_info:exceptiontype": exceptiontype,
#                      "extra_info:comment": comment,
#                      "extra_info:addtime": time,
#                      "raw_data:raw": str(data)})
#     connection.close()

# filter : whether the source data is str

def streamstr(uuid,data):
    if isinstance(data, str) == False:
        exceptiontype = "1"
        comment = "The data  is not a string type."
        exceptiondataupdate(comment,uuid,exceptiontype)
        return False
    return True

# tranform : replace str source data to a normal json
# def streamreplace(data):
#     jsondata = data.replace('''\\''','').replace('''""""''','''""''').replace('''"{''',"{").replace('''}"''', "}")
#     return jsondata

# filter : whether the source data is json format
def streamjson(uuid,data):
    ist = True
    # print(type(data))
    try:
        data_tmp = json.loads(data, encoding='utf-8')
    except:
        exceptiontype = "2"
        comment = "The data  is not a Json format."
        exceptiondataupdate(comment, uuid,exceptiontype)
        # 这里出现异常后，后续不需要再判断measrementItemInfos，直接return。以此类推
        ist =  False

    if ist == True:
        mesurementItemInfos = data_tmp['mesurementItemInfos']
        if type(mesurementItemInfos) == str:

            try:
                json.loads(mesurementItemInfos, encoding='utf-8')
            except:
                exceptiontype = "2"
                comment = "The mesurementItemInfos  is not a Json format."
                exceptiondataupdate(comment, uuid, exceptiontype)
                ist = False

    if ist == True :
        customerInfo = data_tmp['customerInfo']
        if type(customerInfo) == str:
            try:
                json.loads(customerInfo, encoding='utf-8')
            except:
                exceptiontype = "2"
                comment = "The customerInfo  is not a Json format."
                exceptiondataupdate(comment, uuid, exceptiontype)
                ist = False
    return ist

# get shop_no by scan_id
def getShopNo(scan_id):
    sql = "SELECT shop_code FROM scannerlist where scanner_id = '" + scan_id + "' limit 1"
    shop_no = None
    db = None
    try:
        # open the connection
        db = pymysql.connect(host=SCANNERLIST_HOST, port=SCANNERLIST_PORT,
                             user=SCANNERLIST_USER, password=SCANNERLIST_PASSWORD,
                             db=SCANNERLIST_DB, charset=SCANNERLIST_charset)
        #print(db)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist != 0 and ist != None:
            shop_no = cursor.fetchone()[0]
    except:
        # print("no shopNo by scanid")
        logger.info("no shopNo by scanid")
    finally:
        if db:
            db.close()
    return shop_no

# judge shop last exist
def existslast(shop_no):
    shopNo = None
    sql = "SELECT a.shop_no FROM shop_last_inventory a JOIN shop_sku_inventory b  on a.shop_no = b.shop_no and a.styleno = b.styleno and a.basicsize = b.sizes where a.shop_no = '" + shop_no + "' and b.available_qty>0 limit 1"
    db = None
    try:
        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist != 0 and ist != None:
            shopNo = cursor.fetchone()[0]
    except:
        # print("no avaiable last and sku in the shop")
        logger.info("no avaiable last and sku in the shop")
    finally:
        if db:
            db.close()
    if shopNo == None:
        return False
    return True

# # judge shop last exist
# def existsexslast(shop_no,sex):
#     result = False
#     sql = "SELECT shop_no FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + str(sex) + " limit 1"
#     db = None
#     try:
#         db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
#                              user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
#                              db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
#         cursor = db.cursor()
#         ist = cursor.execute(sql)
#         if ist != None and ist > 0:
#             result = True
#     except:
#         print("no avaiable last and sku in the shop")
#     finally:
#         if db:
#             db.close()
#     return result

# judge shop last exist
def existavailablelast(shop_no,sex,sizes):
    result = False
    yearquarter = getyearseason()

    sql = "SELECT shop_no FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + str(sex) + " and year = '" + str(
        yearquarter[0]) + "' and season in " + str(yearquarter[1]) + " and  basicsize in " + str(sizes) + " limit 1"

    db = None
    try:
        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist != None and ist > 0:
            result = True
    except:
        # print("no avaiable last and sku in the shop because of gender or year or season or basicsize ")
        logger.info("no avaiable last and sku in the shop because of gender or year or season or basicsize ")
    finally:
        if db:
            db.close()
    return result



# filter: whether the foot  attribute exist and num and in the normal range
def normal_data_rules(dict,data,UUID):
    footattributes = FOOTATTRIBUTES
    for attribute in footattributes:
        if attribute not in dict:
            exceptiontype = "7"
            comment = attribute + " is not exist."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        if (not isinstance(dict[attribute], float)) and (not isinstance(dict[attribute], int)):
            exceptiontype = "7"
            comment = attribute + " is not num type."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
    # abnormal foot define range
    rules1 = FOOTATTRIBUTES_RULES
    for x in rules1.keys():
        if dict[x] < rules1[x][0] or dict[x] > rules1[x][1] :
            exceptiontype = "8"
            comment = x + " is not in normal range."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
    return True


# filter : foot field
def footfilter(uuid,data):
    # uuid
    if 'UUID' not in data:
        exceptiontype = "3"
        comment = "UUID is not exist."
        exceptiondataupdate( comment, uuid,exceptiontype)
        return False
    UUID = data['UUID']
    if  UUID == None:
        exceptiontype = "3"
        comment = "UUID is  None."
        exceptiondataupdate( comment, uuid,exceptiontype)
        return False
    if UUID == "null":
        exceptiontype = "3"
        comment = "UUID is null."
        exceptiondataupdate( comment, uuid,exceptiontype)
        return False
    if UUID == "":
        exceptiontype = "3"
        comment = "UUID is none."
        exceptiondataupdate( comment, uuid,exceptiontype)
        return False
    # 'mesurementItemInfos', 'customerInfo', 'scanId'
    for field in ['mesurementItemInfos', 'customerInfo', 'scanId']:
        if field not in data:
            exceptiontype = "3"
            comment = field + " is not exist."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        value = data[field]
        if not value:
            exceptiontype = "3"
            comment = field + " is None."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        if value == "null":
            exceptiontype = "3"
            comment = field + " is null."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        if value == "":
            exceptiontype = "3"
            comment = field + " is none."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
    scan_id = data['scanId']
    shop_no = getShopNo(scan_id.split('_')[0])
    if shop_no == None:
        exceptiontype = "4"
        comment = "can not find the shop_no by scan_id."
        exceptiondataupdate( comment, UUID,exceptiontype)
        return False
    if  existslast(shop_no) == False:
        exceptiontype = "5"
        comment = "no last data for computing in the shop"
        exceptiondataupdate(comment,UUID,exceptiontype)
        return False
    customerInfo = data['customerInfo']
    # print(type(customerInfo))
    if type(customerInfo) == str:
        customerInfo = json.loads(customerInfo)
    for customerfield in ['customer_sex', 'algoVersion']:
        if customerfield not in customerInfo:
            exceptiontype = "3"
            comment = customerfield + " is not exist."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        customervalue = customerInfo[customerfield]
        if not customervalue:
            exceptiontype = "3"
            comment = customerfield + " is None."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        if customervalue == "null":
            exceptiontype = "3"
            comment = customerfield + " is null."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
        if customervalue == "":
            exceptiontype = "3"
            comment = customerfield + " is none."
            exceptiondataupdate( comment, UUID,exceptiontype)
            return False
    if customerInfo['customer_sex'] != 2:
        exceptiontype = "3"
        if customerInfo['customer_sex'] == 1:
            comment = "customer_sex is man,cannot compute."
        else:
            comment = "customer_sex is abnormal."
        exceptiondataupdate( comment, UUID,exceptiontype)
        return False
    # if existsexslast(shop_no,customerInfo['customer_sex']) == False:
    #     exceptiontype = "6"
    #     comment = "no avalilable gender last in the shop."
    #     exceptiondataupdate(comment, UUID, exceptiontype)
    #     return False
    mesurementItemInfos = data['mesurementItemInfos']
    # print(type(mesurementItemInfos))
    if type(mesurementItemInfos) == str:
        mesurementItemInfos = json.loads(mesurementItemInfos)

    if len(mesurementItemInfos) != 74:
        exceptiontype = "3"
        comment = "foot data attributes length is not 74. "
        exceptiondataupdate( comment, UUID,exceptiontype)
        return False
    footdata = dict()
    for key, value in mesurementItemInfos.items():
        footdata[key + "_" + "left"] = value['left']
        footdata[key + "_" + "right"] = value['right']
    sizes = []
    foot_length_left = footdata['foot_length_left']
    foot_length_right = footdata['foot_length_right']
    if foot_length_left > foot_length_right:
        foot_length = foot_length_left
    else:
        foot_length = foot_length_right
    sizes = sizes + [foot_length - 10, foot_length - 5, foot_length, foot_length + 5, foot_length + 10]
    for size in sizes:
        if size < 200 or size > 300:
            sizes.remove(size)

    if existavailablelast(shop_no, customerInfo['customer_sex'], tuple(sizes)) == False:
        exceptiontype = "6"
        comment = "no avalilable gender last in the shop."
        exceptiondataupdate(comment, UUID, exceptiontype)
        return False

    if  normal_data_rules(footdata,data,UUID) == False:
       return False
    return True

# get user and foot attributes
def getFootData(data):
    mesurementItemInfos = data['mesurementItemInfos']
    customerInfo = data['customerInfo']
    if type(mesurementItemInfos) == str:
        mesurementItemInfos = json.loads(mesurementItemInfos)
    if type(customerInfo) == str:
        customerInfo = json.loads(customerInfo)

    UUID = data['UUID']
    scanId = data['scanId']

    scanner_id = scanId.split('_')[0]
    shop_no = getShopNo(scanner_id)
    algoVersion = customerInfo['algoVersion']
    customer_sex = customerInfo['customer_sex']

    footdata = dict()
    footdata['shop_no'] = shop_no.strip()
    footdata['UUID'] = UUID
    footdata['algoVersion']=algoVersion
    footdata['customer_sex']=customer_sex
    shop_no_sex = shop_no.strip() + "_" + str(customer_sex)
    for key, value in mesurementItemInfos.items():
        footdata[key + "_" + "left"] = value['left']
        footdata[key + "_" + "right"] = value['right']
    return (shop_no_sex, footdata)

# last data dataetl ============================================
# get last data
# def getlastdata(shop_no_sex):
#     shop_no = shop_no_sex.split('_')[0]
#     sex = shop_no_sex.split('_')[1]
#     lastlist = []
#     sql = "SELECT " + LASTATTRIBUTESSTR + " FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + sex
#     db = None
#     try:
#         db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
#                              user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
#                              db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
#         cursor = db.cursor()
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         for last in result:
#             lasts = getLastDataValue(last)
#             lastlist.append(lasts)
#     except:
#         print("no last data to fecth ")
#     finally:
#         if  db:
#             db.close()
#     return lastlist

# Get the current year season.
def getyearseason():
    yearmonth = time.strftime('%Y%m', time.localtime(time.time()))
    year = yearmonth[3]
    month = int(yearmonth[4:])
    if month >= 3 and month <= 9:
        season = ('A', 'B')
    else:
        season = ('C', 'D')
    return (year,season)
# get last data
def getlastdata(shop_no_sex,sizes):
    shop_no = shop_no_sex.split('_')[0]
    sex = shop_no_sex.split('_')[1]
    lastlist = []
    yearquarter = getyearseason()
    sql = "SELECT " + LASTATTRIBUTESSTR + " FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + sex + " and year = '" + str(
        yearquarter[0]) + "' and season in " + str(yearquarter[1]) + " and  basicsize in " + str(sizes)
    db = None
    try:
        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for last in result:
            lasts = getLastDataValue(last)
            lastlist.append(lasts)
    except:
        # print("no last data to fecth ")
        logger.info("no last data to fecth ")
    finally:
        if  db:
            db.close()
    return lastlist


def getLastDataValue(data):
    last_dimensions = LASTATTRIBUTES
    lastdata = dict()
    index = 0
    for lastfield in last_dimensions:
        lastdata[lastfield] = data[index]
        index = index + 1
    return lastdata


# foot and last data dataetl =================================
# get last data by shopno and foot join last
# def footconnectlast(data):
#     footlasts = list()
#     for shoplast in getlastdata(data[0]):
#         footlasts.append(dict(data[1],**shoplast))
#     return footlasts

def footconnectlast(data):
    sizes = []
    foot_length_left  = data[1]['foot_length_left']
    foot_length_right = data[1]['foot_length_right']
    if foot_length_left > foot_length_right:
        foot_length = foot_length_left
    else:
        foot_length = foot_length_right
    sizes = sizes + [foot_length-10,foot_length-5,foot_length,foot_length+5,foot_length+10]
    for size in sizes:
        if size <200 or size > 300:
            sizes.remove(size)
    footlasts = list()
    for shoplast in getlastdata(data[0],tuple(sizes)):
        footlasts.append(dict(data[1],**shoplast))
    return footlasts

# get the sizeprediction data attributes needed
def footlastetlsave(data):
    footlasttupleslist = list()
    status = 1
    for footlastdict in data:
        UUID = footlastdict['UUID']
        algoVersion = footlastdict['algoVersion']
        shop_no = footlastdict['shop_no']
        styleno = footlastdict['styleno']
        basicsize = footlastdict['basicsize']
        customer_sex = footlastdict['customer_sex']
        dimensions =  FOOT_LAST_ORDER_DIMENSIONS
        userinfo = (status,UUID,algoVersion,shop_no,styleno,basicsize,customer_sex)
        datalist=list()
        for field in dimensions:
            datalist.append(footlastdict[field])
        footlasttuple = userinfo + tuple(datalist)
        footlasttupleslist.append(footlasttuple)
    # print(len(footlasttupleslist))
    logger.info(len(footlasttupleslist))
    res = batchdatasavemysql(footlasttupleslist)
    return res

def batchdatasavemysql(tupledata):
    import pymysql
    db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                         user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                         db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
    cursor = db.cursor()
    sql = "INSERT ignore INTO " + FOOT_LAST_ETL_TABLE + " (" + FOOT_LAST_ORDER_DIMENSIONSSTR + ") VALUES " + FOOT_LAST_ORDER_DIMENSIONSSTR_VALUES
    ist = 0
    try:
        ist = cursor.executemany(sql, tupledata)
        # print(ist)
        db.commit()
        if ist is None:
            ist = 0
    except:
        # traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    return ist

def repetitivedatasave(uuid,footdata):
    import time
    import pymysql
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                         user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                         db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
    cursor = db.cursor()
    value = (uuid,footdata,updatetime)
    sql = "INSERT IGNORE INTO " + FOOT_REPEAT_TABLE + " (uuid,data,updatetime) "+ " VALUES "  + str(value)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
#  return  result
def sendtowx(self,uuid):
    # print('10.start send to port time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    logger.info('10.start send to port time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    returndata = {'uuid': uuid,'res': -1}
    # print(returndata)
    logger.info(returndata)
    try:
        requests.post(RETURN_PORT_URL, data=returndata,timeout=1)
    except requests.ConnectionError as e:
        # print("Send abnormal Connection Timeout.")
        logger.info("Send abnormal Connection Timeout.")
    except requests.ReadTimeout as e:
        # print("Send abnormal Read Timeout")
        logger.info("Send abnormal Read Timeout")
    # print('11.end port return time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logger.info('11.end port return time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))











