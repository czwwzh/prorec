#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import pymysql
import time

# local
from dataetl.etl_configuration import *
from dataetl.util_log import logger
from dataetl.variables import *
from dataetl.util_redis import Redis_db as rds

# online
# from etl_configuration import *
# from util_log import logger
# from variables import *
# from util_redis import Redis_db as rds



# foot data dataetl ============================================
# 将读取的所有数据入库
# sourcedata save
def foot_data_save_mysql(uuid, footdata):
    import time
    import pymysql

    db = None
    cursor = None

    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    value = (uuid,footdata,updatetime)
    sql = "INSERT IGNORE INTO " + FOOT_SCAN_TABLE + " (uuid,data,updatetime) "+ " VALUES "  + str(value)

    ist = 0
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        ist = cursor.execute(sql)
        if ist is None:
            ist = 0
        # 执行sql语句
        db.commit()
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
    return ist

# 异常脚数据更新入库
# exception data save mysql
def exception_data_update(comment, uuid, exceptiontype):
    import pymysql

    db = None
    cursor = None

    sql = "update " + FOOT_SCAN_TABLE +  " set exceptiontype = " + str(exceptiontype) + ", comment = '" + comment + "' where uuid = '" + uuid +"'"

    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except Exception as e:
        logger.info(str(e))
        logger.info("update exception code exception")

    finally:
        if cursor != None:
            # 关闭游标
            cursor.close()
        if db != None:
            # 关闭数据库连接
            db.close()

# 判断传入的脚数据是否为字符串
# filter : whether the source data is str
def stream_str(uuid, data):
    if isinstance(data, str) == False:
        exceptiontype = "1"
        comment = "The data  is not a string type."
        exception_data_update(comment, uuid, exceptiontype)
        return False
    return True


# tranform : replace str source data to a normal json
# def streamreplace(data):
#     jsondata = data.replace('''\\''','').replace('''""""''','''""''').replace('''"{''',"{").replace('''}"''', "}")
#     return jsondata


# filter : whether the source data is json format
def stream_json(uuid, data):
    ist = True
    try:
        data_tmp = json.loads(data, encoding='utf-8')
    except:
        exceptiontype = "2"
        comment = "The source foot data  is not a Json format."
        exception_data_update(comment, uuid, exceptiontype)
        ist =  False

    if ist == True:
        mesurementItemInfos = data_tmp['mesurementItemInfos']
        if type(mesurementItemInfos) == str:
            try:
                json.loads(mesurementItemInfos, encoding='utf-8')
            except:
                exceptiontype = "2"
                comment = "The mesurementItemInfos  is not a Json format."
                exception_data_update(comment, uuid, exceptiontype)
                ist = False

    if ist == True :
        customerInfo = data_tmp['customerInfo']
        if type(customerInfo) == str:
            try:
                json.loads(customerInfo, encoding='utf-8')
            except:
                exceptiontype = "2"
                comment = "The customerInfo  is not a Json format."
                exception_data_update(comment, uuid, exceptiontype)
                ist = False
    return ist

# filter exception foot function define

# 通过scan_id 获取门店号    （是否改为存入redis 哈希表中）
# get shop_no by scan_id
def get_shop_no(scan_id):

    shop_no = None
    db = None
    cursor = None

    sql = "SELECT shop_code FROM scannerlist where scanner_id = '" + scan_id + "' limit 1"

    try:
        db = pymysql.connect(host=SCANNERLIST_HOST, port=SCANNERLIST_PORT,
                             user=SCANNERLIST_USER, password=SCANNERLIST_PASSWORD,
                             db=SCANNERLIST_DB, charset=SCANNERLIST_charset)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist != 0 and ist != None:
            shop_no = cursor.fetchone()[0]
    except Exception as e:
        logger.info(str(e))
        logger.info("no shopNo by scan_id")
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()
    return shop_no


# 判断楦库中是否有相应码段范围、相应性别、当年当季的楦
def exist_available_last(shop_no, sex, sizes):
    result = False
    year_quarter = get_year_sean_from_redis(shop_no)
    if year_quarter[2] == False:
        year_quarter = get_year_sean_from_mysql(shop_no)
        if year_quarter[2] == False:
            return False

    # logger.info(sql)
    db = None
    cursor = None
    try:
        sql = "SELECT shop_no FROM " + LAST_TABLE + " where shop_no = '" + shop_no + "' and gender = " + str(
            sex) + " and year = '" + str(
            year_quarter[0]) + "' and season in " + str(
            tuple(year_quarter[1].split(','))) + " and  basicsize >= " + str(sizes[0]) + " and  basicsize <= " + str(
            sizes[1]) + " limit 1"

        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist != None and ist > 0:
            result = True
    except Exception as e:
        logger.info(str(e))
        logger.info("no avaiable last and sku in the shop because of gender or year or season or basicsize ")
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()
    return result

# 取脚长度（左右脚最大值）上下五个码
def get_sizes(foot_length_original_left,foot_length_original_right):

    size = (foot_length_original_left + foot_length_original_right)/2
    size_min = (int)(size - 10)
    size_max = (int)(size + 10)
    return (size_min,size_max)


# filter: whether the foot  attribute exist and num and in the normal range
def normal_data_rules(dict,UUID):
    footattributes = FOOTATTRIBUTES
    for attribute in footattributes:
        if attribute not in dict:
            exceptiontype = "7"
            comment = attribute + " is not exist."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        if (not isinstance(dict[attribute], float)) and (not isinstance(dict[attribute], int)):
            exceptiontype = "7"
            comment = attribute + " is not num type."
            exception_data_update(comment, UUID, exceptiontype)
            return False
    # abnormal foot define range
    rules1 = FOOTATTRIBUTES_RULES
    for x in rules1.keys():
        if dict[x] < rules1[x][0] or dict[x] > rules1[x][1] :
            exceptiontype = "8"
            comment = x + " is not in normal range."
            exception_data_update(comment, UUID, exceptiontype)
            return False
    return True


# filter : foot field
def footfilter(uuid,data):
    # 判断json对象第一层所需字段是否异常
    # uuid
    if 'UUID' not in data:
        exceptiontype = "3"
        comment = "UUID is not exist."
        exception_data_update(comment, uuid, exceptiontype)
        return False
    UUID = data['UUID']
    if  UUID == None:
        exceptiontype = "3"
        comment = "UUID is  None."
        exception_data_update(comment, uuid, exceptiontype)
        return False
    if UUID == "null":
        exceptiontype = "3"
        comment = "UUID is null."
        exception_data_update(comment, uuid, exceptiontype)
        return False
    if UUID == "":
        exceptiontype = "3"
        comment = "UUID is none."
        exception_data_update(comment, uuid, exceptiontype)
        return False
    # 'mesurementItemInfos', 'customerInfo', 'scanId'
    for field in ['mesurementItemInfos', 'customerInfo', 'scanId']:
        if field not in data:
            exceptiontype = "3"
            comment = field + " is not exist."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        value = data[field]
        if not value:
            exceptiontype = "3"
            comment = field + " is None."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        if value == "null":
            exceptiontype = "3"
            comment = field + " is null."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        if value == "":
            exceptiontype = "3"
            comment = field + " is none."
            exception_data_update(comment, UUID, exceptiontype)
            return False

    # 判断门店scanId是否有对应门店
    scan_id = data['scanId']
    shop_no = get_shop_no(scan_id.split('_')[0])
    if shop_no == None:
        exceptiontype = "4"
        comment = "can not find the shop_no by scan_id."
        exception_data_update(comment, UUID, exceptiontype)
        return False

    # 用户信息字段是否异常
    customerInfo = data['customerInfo']
    if type(customerInfo) == str:
        customerInfo = json.loads(customerInfo)
    for customerfield in ['customer_sex', 'algoVersion']:
        if customerfield not in customerInfo:
            exceptiontype = "3"
            comment = customerfield + " is not exist."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        customervalue = customerInfo[customerfield]
        if not customervalue:
            exceptiontype = "3"
            comment = customerfield + " is None."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        if customervalue == "null":
            exceptiontype = "3"
            comment = customerfield + " is null."
            exception_data_update(comment, UUID, exceptiontype)
            return False
        if customervalue == "":
            exceptiontype = "3"
            comment = customerfield + " is none."
            exception_data_update(comment, UUID, exceptiontype)
            return False
    if customerInfo['customer_sex'] != 2:
        exceptiontype = "3"
        if customerInfo['customer_sex'] == 1:
            comment = "man cannot be computed in this version."
        else:
            comment = "customer_sex is abnormal."
        exception_data_update(comment, UUID, exceptiontype)
        return False

    # 脚数据字段是否异常
    mesurementItemInfos = data['mesurementItemInfos']
    if type(mesurementItemInfos) == str:
        mesurementItemInfos = json.loads(mesurementItemInfos)
    if len(mesurementItemInfos) != 74:
        exceptiontype = "3"
        comment = "foot data attributes length is not 74. "
        exception_data_update(comment, UUID, exceptiontype)
        return False
    footdata = dict()
    for key, value in mesurementItemInfos.items():
        footdata[key + "_" + "left"] = value['left']
        footdata[key + "_" + "right"] = value['right']
    if  normal_data_rules(footdata,UUID) == False:
       return False

    # 取脚长度（左右脚最大值）上下五个码，这里用于判断库存
    sizes = get_sizes(footdata['foot_length_original_left'],footdata['foot_length_original_right'])
    # 判断楦库中是否有相应码段范围、相应性别、当年当季的楦
    if exist_available_last(shop_no, customerInfo['customer_sex'], sizes) == False:
        exceptiontype = "5"
        comment = "no avalilable  last in the shop."
        exception_data_update(comment, UUID, exceptiontype)
        return False

    return True

# 脚数据获取与解析
# get user info and foot attributes
def get_foot_data(data):
    mesurementItemInfos = data['mesurementItemInfos']
    customerInfo = data['customerInfo']
    if type(mesurementItemInfos) == str:
        mesurementItemInfos = json.loads(mesurementItemInfos)
    if type(customerInfo) == str:
        customerInfo = json.loads(customerInfo)

    UUID = data['UUID']
    scanId = data['scanId']

    scanner_id = scanId.split('_')[0]
    shop_no = get_shop_no(scanner_id)
    algoVersion = customerInfo['algoVersion']
    customer_sex = customerInfo['customer_sex']

    footdata = dict()
    footdata['shop_no'] = shop_no.strip()
    footdata['UUID'] = UUID
    footdata['algoVersion']=algoVersion
    footdata['customer_sex']=customer_sex
    for key, value in mesurementItemInfos.items():
        footdata[key + "_" + "left"] = value['left']
        footdata[key + "_" + "right"] = value['right']
    return footdata

# last data dataetl ============================================
# 获取当前门店商品的主要两个季
def get_year_sean_from_redis(shop_no):
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


# 从mysql中获取当前门店商品的主要两个季
def get_year_sean_from_mysql(shop_no):
    cursor = None
    db = None

    result = None
    flag = True
    year = time.strftime('%Y', time.localtime(time.time()))
    year = year[3]

    sql = "SELECT season" +  " FROM " + SHOP_SEASON_TABLE + " where shop_no = '" + shop_no + "'  limit 1"
    try:

        db = pymysql.connect(host=SKU_LAST_URL, port=SKU_LAST_PORT,
                             user=SKU_LAST_USER, password=SKU_LAST_PASSWORD,
                             db=SKU_LAST_DB, charset=SKU_LAST_CHARSET)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
    except Exception as e:
        flag = False
        logger.info("can't fetch shop season from mysql")
        logger.info(str(e))
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()
    return (year,result,flag)


# 重复uuid入库
def repetive_data_save(uuid, footdata):
    import time
    import pymysql

    db = None
    cursor = None

    updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    value = (uuid,footdata,updatetime)
    sql = "INSERT IGNORE INTO " + FOOT_REPEAT_TABLE + " (uuid,data,updatetime) "+ " VALUES "  + str(value)
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except Exception as e:
        logger.info(str(e))
        logger.info("save repeative data exception")
    finally:
        if cursor != None:
            cursor.close()
        if db != None:
            db.close()











