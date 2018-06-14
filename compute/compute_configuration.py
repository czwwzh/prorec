#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas


# --------------hbase configuration---------------
HBASE_HOST = '52.80.170.199'
HBASE_TIMEOUT = 10000
HBASE_PORT = 9090
HBASE_PROTOCOL = 'binary'
HBASE_TRANSPORT = 'buffered'
# online
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'
# test
HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest3'




# ---------------model configuration-------------
# # online
# # model
# SUIT2MODELPATH = '/suitmodel/lgbm_2'
# SUIT6MODELPATH = '/suitmodel/lgbm_6'
# SUIT12MODELPATH = '/suitmodel/lgbm_12'
#
# # preprocess data
# SUIT2PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_2'
# SUIT6PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_6'
# SUIT12PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_12'
#
# suit compute attributes
# SUIT_LEFT = '/suitmodel/suit_left'
# SUIT_RIGHT = '/suitmodel/suit_right'

# # size model
# # model
# SIZEMODEL0PATH = '/sizemodel-2/lgbm_shoe_0'
# SIZEMODEL1PATH = '/sizemodel-2/lgbm_shoe_1'
# SIZEMODEL2PATH = '/sizemodel-2/lgbm_shoe_2'
# SIZEMODEL3PATH = '/sizemodel-2/lgbm_shoe_3'
# SIZEMODEL4PATH = '/sizemodel-2/stack_lgbm_shoe'
# # data preprocess function
# SIZESTANDARDSCALER0PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_0'
# SIZESTANDARDSCALER1PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_1'
# SIZESTANDARDSCALER2PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_2'
# SIZESTANDARDSCALER3PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_3'
# # size compute attributes
# SIZE_DIMENSION_NAME = '/sizemodel-2/size_dimension_name'


# local
# model
SUIT2MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_2'
SUIT6MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_6'
SUIT12MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_12'

# preprocess data
SUIT2PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_2'
SUIT6PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_6'
SUIT12PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_12'

# suit compute attributes
SUIT_LEFT = 'D:\\recommend\models\woman\\v1\suit\suit_left'
SUIT_RIGHT = 'D:\\recommend\models\woman\\v1\suit\suit_right'

# size model
# model
SIZEMODEL0PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_0'
SIZEMODEL1PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_1'
SIZEMODEL2PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_2'
SIZEMODEL3PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_3'
SIZEMODEL4PATH = 'D:\\recommend\models\woman\\v1\size\stack_lgbm_shoe'
# data preprocess function
SIZESTANDARDSCALER0PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_0'
SIZESTANDARDSCALER1PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_1'
SIZESTANDARDSCALER2PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_2'
SIZESTANDARDSCALER3PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_3'
# size compute attributes
SIZE_DIMENSION_NAME = 'D:\\recommend\models\woman\\v1\size\size_dimension_name'



# --------redis configuration------------------
# online
# REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
# local
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
REDIS_LIST_FOOT_LAST_ETL = 'redis_list_footdata_etl'
# 正常数据进入的hash队列名称
REDIS_HASHSET_FOOT_LAST_ETL = 'redis_hashset_footdata_etl'
# 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
REDIS_LIST_COMPUTE_RESULT = 'redis_list_compute_result'
# 模型计算完成数据进入的redis 哈希表名称
REDIS_HASHSET_COMPUTE_RESULT = 'redis_hashset_compute_result'
# 模型计算完将uuid放入redis队列，用于etl数据存储
REDIS_LIST_ETL_SAVE = 'redis_list_etl_save'



# ----LOG PATH-------------------
LOG_FILE_PATH ='D:\\recommend\prodrec\log\model_compute_'

# ------------模型计算所用变量定义-------------
# size模型所需字段顺序定义
# variables define
FOOT_LAST_ORDER_DIMENSIONS = pandas.read_pickle(SIZE_DIMENSION_NAME)
# 左脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_LEFT_DIMENSIONS = pandas.read_pickle(SUIT_LEFT).tolist()
# 右脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_RIGHT_DIMENSIONS = pandas.read_pickle(SUIT_RIGHT).tolist()


