#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# spark python model redis hbase last
from variables import *


# ===============configuration common===================
# last data common configuration for sparksql and pymysql
SPARKSQL_DRIVER = "com.mysql.jdbc.Driver"
SPARKSQL_LAST_URL = "jdbc:mysql://epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn:60916/bdp_products"
SKU_LAST_URL = "epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SKU_LAST_USER = "haozhShopRecom"
SKU_LAST_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
SKU_LAST_PORT = 60916
SKU_LAST_DB = "bdp_products"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
# FOOT_LAST_ETL_TABLE = "footlastetl"
FOOT_DATA_TABLE = 'foot_scan'
FOOT_REPEATDATA_TABLE = 'foot_repeat'

# sku recommend dataetl and compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_NAME = 'shop_sku_recommend'
# RECOMMEND_DB_NAME = 'bdp_products'
RECOMMEND_DB_CHARSET = 'utf8mb4'

FOOT_LAST_ETL_TABLE = 'foot_last_etl'
FOOT_SCAN_TABLE = 'foot_scan'
FOOT_REPEAT_TABLE = 'foot_repeat'


#hbase common configuration
HBASE_TIMEOUT = 10000
HBASE_PORT = 9090
HBASE_PROTOCOL = 'binary'
HBASE_TRANSPORT = 'buffered'
HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawException'
HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'
# HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawExceptionTest'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest'

# scannerlist
SCANNERLIST_HOST = "epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SCANNERLIST_PORT = 60916
SCANNERLIST_USER = "haozhangRead"
SCANNERLIST_PASSWORD = "haozhangRead_45ediU7yb9v3"
SCANNERLIST_DB = "epoque_boss"
SCANNERLIST_charset = "utf8mb4"



# ===============configuration for local===================
# hbase local
HBASE_HOST = '52.80.170.199'

# redis local
# local
# REDIS_HOST = '192.168.17.110'
# test
# REDIS_HOST = '54.222.142.37'
# prod
# REDIS_HOST = '54.222.142.37'
REDIS_HOST = '52.80.200.237'
REDIS_PORT = 6379
CHAN_SUB = 'uuidtransfernew0'
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':1}


# kafka configuration
KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
KAFKA_PROD_FOOTTOPIC = 'footInfoProd'
KAFKA_GROUP_ID = 'footInfoProd12'
KAFKA_GROUP_ID_SIZE = "sizelocal"
KAFKA_GROUP_ID_SUIT2 = "suit2local"
KAFKA_GROUP_ID_SUIT6 = "suit6local"
KAFKA_GROUP_ID_SUIT12 = "suit12local"
KAFKA_GROUP_ID_SUIT2612 = "suit2612local"
KAFKA_GROUP_ID_SIZE_SUIT2612 = "sizesuit2612local"

# last sql
LAST_DBTABLE = "(SELECT " + LASTATTRIBUTESSTR + " FROM shop_last_inventory) shop_last_tmp"
