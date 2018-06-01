#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# spark python model redis hbase last
from variables import *

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# ===============configuration common===================
# configuration for data etl
# mysql connection
# scannerlist
SCANNERLIST_HOST = "epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SCANNERLIST_PORT = 60916
SCANNERLIST_USER = "haozhangRead"
SCANNERLIST_PASSWORD = "haozhangRead_45ediU7yb9v3"
SCANNERLIST_DB = "epoque_boss"
SCANNERLIST_charset = "utf8mb4"

# sku recommend dataetl and compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_CHARSET = 'utf8mb4'
# prod db
# RECOMMEND_DB_NAME = 'shop_sku_recommend'
# test db
RECOMMEND_DB_NAME = 'bdp_products'

# FOOT_LAST_ETL_TABLE = 'foot_last_etl'
# FOOT_SCAN_TABLE = 'foot_scan'
# FOOT_REPEAT_TABLE = 'foot_repeat'

FOOT_LAST_ETL_TABLE = 'foot_last_etl_test'
FOOT_SCAN_TABLE = 'foot_scan_test'
FOOT_REPEAT_TABLE = 'foot_repeat_test'

# sku and last
# test
# SKU_LAST_USER = "haozhShopRecom"
# SKU_LAST_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
# SKU_LAST_PORT = 60916
# SKU_LAST_DB = "bdp_products"
# SKU_LAST_CHARSET='utf8mb4'
# LAST_TABLE = 'shop_last_inventory'
# SKU_TABLE = 'shop_sku_inventory'
# LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}

# prod
SKU_LAST_URL = "private02.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SKU_LAST_USER = "haozhFattypeRecom"
SKU_LAST_PASSWORD = "haozhangShopSkuLast_2U89Tzs4ERMu"
SKU_LAST_PORT = 61539
SKU_LAST_DB = "fattype_recommend"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
SKU_TABLE = 'shop_sku_inventory'
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}


# redis connection
# local
# REDIS_HOST = '192.168.17.110'
# prod
# REDIS_HOST = '54.222.236.85'
# REDIS_HOST = 'prod-sku-recommend.rawr9u.clustercfg.cnn1.cache.amazonaws.com.cn'
REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
# REDIS_HOST = '52.80.83.193'
REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}


# kafka configuration
# prod
KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
KAFKA_PROD_FOOTTOPIC = 'footInfoProd'
# test
# KAFKA_PROD_FOOTTOPIC = 'footcom'
KAFKA_GROUP_ID = 'footInfoProdprod33'


# return url
# test
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# prod
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# compute completed return host
# RETURN_PORT_URL = 'http://54.222.142.37:9998/shopRecommendController/test'

logFilePath = '/home/ec2-user/zhanghao/log/dataetllog'
