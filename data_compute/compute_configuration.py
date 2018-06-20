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
HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'
# test
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest3'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest'


# 楦数据
# test
# SKU_LAST_URL = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
# SKU_LAST_USER = "haozhShopRecom"
# SKU_LAST_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
# SKU_LAST_PORT = 60916
# SKU_LAST_DB = "bdp_products"
# SKU_LAST_CHARSET='utf8mb4'
# LAST_TABLE = 'shop_last_inventory'
# SKU_TABLE = 'shop_sku_inventory'
# LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
# SHOP_SEASON_TABLE  = 'shop_season_statistics'

# online
SKU_LAST_URL = "private02.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn"
SKU_LAST_USER = "haozhFattypeRecom"
SKU_LAST_PASSWORD = "haozhangShopSkuLast_2U89Tzs4ERMu"
SKU_LAST_PORT = 61539
SKU_LAST_DB = "fattype_recommend"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
SKU_TABLE = 'shop_sku_inventory'
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
SHOP_SEASON_TABLE  = 'shop_season_statistics'


# ---------------model configuration-------------
# # online
# model
SUIT2MODELPATH = '/models/woman/v1/suit/lgbm_2'
SUIT6MODELPATH = '/models/woman/v1/suit/lgbm_6'
SUIT12MODELPATH = '/models/woman/v1/suit/lgbm_12'

# preprocess data
SUIT2PREPROCESSPATH = '/models/woman/v1/suit/StandardScaler_lgbm_2'
SUIT6PREPROCESSPATH = '/models/woman/v1/suit/StandardScaler_lgbm_6'
SUIT12PREPROCESSPATH = '/models/woman/v1/suit/StandardScaler_lgbm_12'

# suit data_compute attributes
SUIT_LEFT = '/models/woman/v1/suit/suit_left'
SUIT_RIGHT = '/models/woman/v1/suit/suit_right'

# size model
# model
SIZEMODEL0PATH = '/models/woman/v1/size/lgbm_shoe_0'
SIZEMODEL1PATH = '/models/woman/v1/size/lgbm_shoe_1'
SIZEMODEL2PATH = '/models/woman/v1/size/lgbm_shoe_2'
SIZEMODEL3PATH = '/models/woman/v1/size/lgbm_shoe_3'
SIZEMODEL4PATH = '/models/woman/v1/size/stack_lgbm_shoe'
# data preprocess function
SIZESTANDARDSCALER0PATH = '/models/woman/v1/size/StandardScaler_lgbm_shoe_0'
SIZESTANDARDSCALER1PATH = '/models/woman/v1/size/StandardScaler_lgbm_shoe_1'
SIZESTANDARDSCALER2PATH = '/models/woman/v1/size/StandardScaler_lgbm_shoe_2'
SIZESTANDARDSCALER3PATH = '/models/woman/v1/size/StandardScaler_lgbm_shoe_3'
# size data_compute attributes
SIZE_DIMENSION_NAME = '/models/woman/v1/size/size_dimension_name'


# local
# model
# SUIT2MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_2'
# SUIT6MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_6'
# SUIT12MODELPATH = 'D:\\recommend\models\woman\\v1\suit\lgbm_12'
#
# # preprocess data
# SUIT2PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_2'
# SUIT6PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_6'
# SUIT12PREPROCESSPATH = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_12'
#
# # suit data_compute attributes
# SUIT_LEFT = 'D:\\recommend\models\woman\\v1\suit\suit_left'
# SUIT_RIGHT = 'D:\\recommend\models\woman\\v1\suit\suit_right'
#
# # size model
# # model
# SIZEMODEL0PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_0'
# SIZEMODEL1PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_1'
# SIZEMODEL2PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_2'
# SIZEMODEL3PATH = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_3'
# SIZEMODEL4PATH = 'D:\\recommend\models\woman\\v1\size\stack_lgbm_shoe'
# # data preprocess function
# SIZESTANDARDSCALER0PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_0'
# SIZESTANDARDSCALER1PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_1'
# SIZESTANDARDSCALER2PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_2'
# SIZESTANDARDSCALER3PATH = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_3'
# # size data_compute attributes
# SIZE_DIMENSION_NAME = 'D:\\recommend\models\woman\\v1\size\size_dimension_name'



# --------redis configuration------------------
# online
REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'

# local
# REDIS_HOST = '52.80.137.153'
REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}
# etl之后的脚数据集合进入的队列名称
REDIS_LIST_FOOT_ETL = 'redis_list_foot_etl'
# 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
REDIS_LIST_COMPUTE_RESULT = 'redis_list_compute_result'
# 门店季节
REDIS_HASHSET_SHOP_SEASON = 'redis_hashset_shop_season'


# ----LOG PATH-------------------
LOG_FILE_PATH ='/home/ec2-user/zhanghao/log/model_compute_'

# ------------模型计算所用变量定义-------------
# size模型所需字段顺序定义
# variables define
FOOT_LAST_ORDER_DIMENSIONS = pandas.read_pickle(SIZE_DIMENSION_NAME)
# 左脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_LEFT_DIMENSIONS = pandas.read_pickle(SUIT_LEFT).tolist()
# 右脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_RIGHT_DIMENSIONS = pandas.read_pickle(SUIT_RIGHT).tolist()







