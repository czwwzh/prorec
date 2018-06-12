# LOG PATH
LOG_FILE_PATH ='D:\\recommend\prodrec\log\data_convert_catche_'




# kafka configuration
# prod
KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
KAFKA_PROD_FOOTTOPIC = 'footInfoProd'
# test
# KAFKA_PROD_FOOTTOPIC = 'footcom'
KAFKA_GROUP_ID = 'footInfoProdprodTest0612'



# redis configuration
# local
# REDIS_HOST = '192.168.17.110'

# test1
# REDIS_HOST = '54.222.236.85'

# test2
# REDIS_HOST = 'prod-sku-recommend.rawr9u.clustercfg.cnn1.cache.amazonaws.com.cn'

# test3
REDIS_HOST = '52.80.137.153'

# prod
# REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
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

# return url
# test
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# prod
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# compute completed return host
# RETURN_PORT_URL = 'http://54.222.142.37:9998/shopRecommendController/test'