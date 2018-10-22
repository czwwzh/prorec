#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 1.门店列表库
SCANNERLIST_HOST = "10.240.18.137"
SCANNERLIST_PORT = 3306
SCANNERLIST_USER = "root"
SCANNERLIST_PASSWORD = "epoque@belle1qaz"
SCANNERLIST_DB = "epoque_rds"
SCANNERLIST_charset = "utf8mb4"


# 2.预处理所用库配置
RECOMMEND_DB_HOST = '10.240.18.136'
RECOMMEND_DB_PORT = 3306
RECOMMEND_DB_CHARSET = 'utf8mb4'
RECOMMEND_DB_USER = "root"
RECOMMEND_DB_PASSWORD = "epoque@belle1qaz"
RECOMMEND_DB_NAME = 'epoque_rds'
FOOT_SCAN_TABLE = 'foot_scan'
FOOT_REPEAT_TABLE = 'foot_repeat'



# 3.门店商品库 门店楦库
# 线上所用库
SKU_LAST_URL = "10.240.18.137"
SKU_LAST_USER = "root"
SKU_LAST_PASSWORD = "epoque@belle1qaz"
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
SKU_LAST_PORT = 3306
SKU_LAST_DB = "epoque_rds"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
SKU_TABLE = 'shop_sku_inventory'
SHOP_SEASON_TABLE  = 'shop_season_statistics'

# 4. redis配置
REDIS_HOST = '10.240.117.16'
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


# 5.日志文件地址
# 日志线上路径
LOG_FILE_PATH ='/root/log/recommend/data_etl_'



