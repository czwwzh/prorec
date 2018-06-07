#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# spark python model redis hbase last


# sku recommend dataetl and compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_NAME = 'shop_sku_recommend'
# RECOMMEND_DB_NAME = 'bdp_products'
RECOMMEND_DB_CHARSET = 'utf8mb4'
FOOT_LAST_ETL_TABLE = 'foot_last_etl'

#hbase configuration
# HBASE_HOST = '52.80.170.199'
HBASE_HOST = '54.222.249.145'
HBASE_TIMEOUT = 10000
HBASE_PORT = 9090
HBASE_PROTOCOL = 'compact'
HBASE_TRANSPORT = 'framed'
# prod
HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawException'
HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'

# test
# HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawExceptionTest'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest3'

# model
SUIT2MODELPATH = '/suitmodel/lgbm_2'
SUIT6MODELPATH = '/suitmodel/lgbm_6'
SUIT12MODELPATH = '/suitmodel/lgbm_12'

# preprocess data
SUIT2PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_2'
SUIT6PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_6'
SUIT12PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_12'

# size model
# model
SIZEMODEL0PATH = '/sizemodel-2/lgbm_shoe_0'
SIZEMODEL1PATH = '/sizemodel-2/lgbm_shoe_1'
SIZEMODEL2PATH = '/sizemodel-2/lgbm_shoe_2'
SIZEMODEL3PATH = '/sizemodel-2/lgbm_shoe_3'
SIZEMODEL4PATH = '/sizemodel-2/stack_lgbm_shoe'
# data preprocess function
SIZESTANDARDSCALER0PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_0'
SIZESTANDARDSCALER1PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_1'
SIZESTANDARDSCALER2PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_2'
SIZESTANDARDSCALER3PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_3'

# redis connection
# local
# REDIS_HOST = '192.168.17.110'
# prod
# REDIS_HOST = '54.222.236.85'
# REDIS_HOST = '52.80.83.193'
REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
# REDIS_HOST = 'prod-sku-recommend.rawr9u.clustercfg.cnn1.cache.amazonaws.com.cn'
REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}




# return url
# test
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# prod
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# compute completed return host
# RETURN_PORT_URL = 'http://54.222.142.37:9998/shopRecommendController/test'

logFilePath = '/home/ec2-user/zhanghao/log/computelog/modelcompute_v1.0'





