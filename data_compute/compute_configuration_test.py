#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas
#1.  Hbase 的配置hbase configuration
HBASE_HOST = '52.80.170.199'
HBASE_TIMEOUT = 10000
HBASE_PORT = 9090
HBASE_PROTOCOL = 'binary'
HBASE_TRANSPORT = 'buffered'
# Hbase线上使用的表
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'
# Hbase测试使用的表
HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest'
#______________________________________________________________________

#2. 门店楦库配置
# 门店楦库测试使用表
SKU_LAST_URL = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
SKU_LAST_USER = "zhanghaoDev"
SKU_LAST_PASSWORD = "zhanghaoDevelop_38Yup9Bc5Ew7"
SKU_LAST_PORT = 60916
SKU_LAST_DB = "haozhang"
SKU_LAST_CHARSET='utf8mb4'
LAST_TABLE = 'shop_last_inventory'
SKU_TABLE = 'shop_sku_inventory'
LAST_PROPERTIES = {'user':SKU_LAST_USER,'password':SKU_LAST_PASSWORD}
SHOP_SEASON_TABLE  = 'shop_season_statistics'
#______________________________________________________________________


#3.模型配置
# woman
# size :  model，data preprocess function，attributes
SIZE_MODEL0_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_0'
SIZE_MODEL1_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_1'
SIZE_MODEL2_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_2'
SIZE_MODEL3_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\lgbm_shoe_3'
SIZE_MODEL4_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\stack_lgbm_shoe'
SIZE_STANDARDSCALER0_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_0'
SIZE_STANDARDSCALER1_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_1'
SIZE_STANDARDSCALER2_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_2'
SIZE_STANDARDSCALER3_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\size\StandardScaler_lgbm_shoe_3'
SIZE_DIMENSION_NAME_WOMAN = 'D:\\recommend\models\woman\\v1\size\size_dimension_name'
# suit :  model，data preprocess function，attributes
SUIT2_MODEL_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\lgbm_2'
SUIT6_MODEL_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\lgbm_6'
SUIT12_MODEL_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\lgbm_12'
SUIT2_PREPROCESS_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_2'
SUIT6_PREPROCESS_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_6'
SUIT12_PREPROCESS_PATH_WOMAN = 'D:\\recommend\models\woman\\v1\suit\StandardScaler_lgbm_12'
SUIT_LEFT_WOMAN = 'D:\\recommend\models\woman\\v1\suit\suit_left'
SUIT_RIGHT_WOMAN = 'D:\\recommend\models\woman\\v1\suit\suit_right'

#man
# suit :  model，data preprocess function，attributes
SUIT2_MODEL_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\lgbm_2_man'
SUIT6_MODEL_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\lgbm_6_man'
SUIT12_MODEL_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\lgbm_12_man'
SUIT2_PREPROCESS_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\StandardScaler_lgbm_2_man'
SUIT6_PREPROCESS_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\StandardScaler_lgbm_6_man'
SUIT12_PREPROCESS_PATH_MAN = 'D:\\recommend\models\man\\v1\suit\StandardScaler_lgbm_12_man'
SUIT_LEFT_MAN = 'D:\\recommend\models\woman\\v1\suit\suit_left'
SUIT_RIGHT_MAN = 'D:\\recommend\models\woman\\v1\suit\suit_right'
# size: model，data preprocess function，attributes
SIZE_StandardScaler_MLP_PATH0_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_mlp_shoe_0_man'
SIZE_StandardScaler_MLP_PATH1_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_mlp_shoe_1_man'
SIZE_StandardScaler_MLP_PATH2_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_mlp_shoe_2_man'
SIZE_MODEL_MLP_PATH0_MAN = 'D:\\recommend\models\man\\v1\size\mlp_shoe_0_man'
SIZE_MODEL_MLP_PATH1_MAN = 'D:\\recommend\models\man\\v1\size\mlp_shoe_1_man'
SIZE_MODEL_MLP_PATH2_MAN = 'D:\\recommend\models\man\\v1\size\mlp_shoe_2_man'
SIZE_MODEL_STACK_MLP_PATH_MAN = 'D:\\recommend\models\man\\v1\size\stack_mlp_shoe_man'
SIZE_StandardScaler_LGBM_PATH0_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_lgbm_shoe_0_man'
SIZE_StandardScaler_LGBM_PATH1_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_lgbm_shoe_1_man'
SIZE_StandardScaler_LGBM_PATH2_MAN = 'D:\\recommend\models\man\\v1\size\StandardScaler_lgbm_shoe_2_man'
SIZE_MODEL_LGBM_PATH0_MAN = 'D:\\recommend\models\man\\v1\size\lgbm_shoe_0_man'
SIZE_MODEL_LGBM_PATH1_MAN = 'D:\\recommend\models\man\\v1\size\lgbm_shoe_1_man'
SIZE_MODEL_LGBM_PATH2_MAN = 'D:\\recommend\models\man\\v1\size\lgbm_shoe_2_man'
SIZE_DIMENSION_NAME_MAN = 'D:\\recommend\models\man\\v1\size\size_dimension_name'
#______________________________________________________________________


# 4. redis配置
# prod
# REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
# test
REDIS_HOST = '54.222.235.154'

REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}
# etl之后的脚数据集合进入的队列名称
REDIS_LIST_FOOT_ETL = 'redis_list_foot_etl'
# 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
REDIS_LIST_COMPUTE_RESULT = 'redis_list_compute_result'
# 门店季节
REDIS_HASHSET_SHOP_SEASON = 'redis_hashset_shop_season'


# 5.日志文件地址
# 本地日志路径
LOG_FILE_PATH ='D:\\recommend\prodrec\log\model_compute_'


# 6.模型计算所用变量
# woman
# variables define
FOOT_LAST_ORDER_DIMENSIONS_MAN = pandas.read_pickle(SIZE_DIMENSION_NAME_MAN)
# 左脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_LEFT_DIMENSIONS_MAN = pandas.read_pickle(SUIT_LEFT_MAN).tolist()
# 右脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_RIGHT_DIMENSIONS_MAN = pandas.read_pickle(SUIT_RIGHT_MAN).tolist()
# man
# variables define
FOOT_LAST_ORDER_DIMENSIONS = pandas.read_pickle(SIZE_DIMENSION_NAME_WOMAN)
# 左脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_LEFT_DIMENSIONS = pandas.read_pickle(SUIT_LEFT_WOMAN).tolist()
# 右脚舒适度模型所需字段顺序定义
FOOT_LAST_ORDER_RIGHT_DIMENSIONS = pandas.read_pickle(SUIT_RIGHT_WOMAN).tolist()








