#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# # test
# # configuration for data etl
# # mysql connection
# # ====门店列表库====
# # scannerlist
# SCANNERLIST_HOST = "epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
# SCANNERLIST_PORT = 60916
# SCANNERLIST_USER = "haozhangRead"
# SCANNERLIST_PASSWORD = "haozhangRead_45ediU7yb9v3"
# SCANNERLIST_DB = "epoque_boss"
# SCANNERLIST_charset = "utf8mb4"
#
# #  ====预处理所用表====
# # sku recommend dataetl and data_compute table
# RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
# RECOMMEND_DB_PORT = 60916
# RECOMMEND_DB_USER = "haozhShopRecom"
# RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
# RECOMMEND_DB_CHARSET = 'utf8mb4'

RECOMMEND_DB_NAME = 'bdp_products'
FOOT_SCAN_TABLE = 'foot_scan_test'
FOOT_REPEAT_TABLE = 'foot_repeat_test'
#
#
# # 门店商品库 门店楦库
# # sku and last
#
# # test
# SKU_LAST_URL = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
# SKU_LAST_USER = "haozhShopRecom"
# SKU_LAST_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
# SKU_LAST_PORT = 60916
# SKU_LAST_DB = "bdp_products"
# SKU_LAST_CHARSET='utf8mb4'
# LAST_TABLE = 'shop_last_inventory'
# SKU_TABLE = 'shop_sku_inventory'
# SHOP_SEASON_TABLE  = 'shop_season_statistics'
# LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
#
#
#
# #  ===redis connection ====
# REDIS_HOST = '52.80.137.153'
# REDIS_PORT = 6379
# REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}
# # kafka 数据转入redis中的对列名 uuid
# REDIS_KAFKA_LIST = 'kafka_redis_list_data'
# # kafka 数据转入redis中的哈希表名 uuid footdata
# REDIS_KAFKA_HASHSET = 'kafka_redis_hash_data'
# # 异常脚数据存入redis的队列名称
# REDIS_LIST_FOOTDATA_EXCEPT = 'redis_list_footdata_except'
# # 正常数据uuid进入的队列名称
# REDIS_LIST_FOOT_ETL = 'redis_list_foot_etl'
# # 门店季节
# REDIS_HASHSET_SHOP_SEASON = 'redis_hashset_shop_season'
#
#
#
#
# # LOG PATH
# LOG_FILE_PATH ='D:\\recommend\prodrec\log\data_etl_'




# mysql connection
# ====门店列表库====
# scannerlist
SCANNERLIST_HOST = "epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SCANNERLIST_PORT = 60916
SCANNERLIST_USER = "haozhangRead"
SCANNERLIST_PASSWORD = "haozhangRead_45ediU7yb9v3"
SCANNERLIST_DB = "epoque_boss"
SCANNERLIST_charset = "utf8mb4"

#  ====预处理所用表====
# sku recommend dataetl and data_compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_CHARSET = 'utf8mb4'

# RECOMMEND_DB_NAME = 'shop_sku_recommend'
# FOOT_SCAN_TABLE = 'foot_scan'
# FOOT_REPEAT_TABLE = 'foot_repeat'



# 门店商品库 门店楦库
# sku and last
SKU_LAST_URL = "private02.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SKU_LAST_USER = "haozhFattypeRecom"
SKU_LAST_PASSWORD = "haozhangShopSkuLast_2U89Tzs4ERMu"
SKU_LAST_PORT = 61539
SKU_LAST_DB = "fattype_recommend"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
SKU_TABLE = 'shop_sku_inventory'
SHOP_SEASON_TABLE  = 'shop_season_statistics'
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}


#  ===redis connection ====
REDIS_HOST = '52.80.137.153'
REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}
# kafka 数据转入redis中的对列名 uuid
REDIS_KAFKA_LIST = 'kafka_redis_list_data'
# kafka 数据转入redis中的哈希表名 uuid footdata
REDIS_KAFKA_HASHSET = 'kafka_redis_hash_data'
# 异常脚数据存入redis的队列名称
REDIS_LIST_FOOTDATA_EXCEPT = 'redis_list_footdata_except'
# 正常数据uuid进入的队列名称
REDIS_LIST_FOOT_ETL = 'redis_list_foot_etl'
# 门店季节
REDIS_HASHSET_SHOP_SEASON = 'redis_hashset_shop_season'

# LOG PATH
LOG_FILE_PATH = '/home/ec2-user/zhanghao/log/data_etl_'

