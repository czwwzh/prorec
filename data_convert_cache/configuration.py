# test

# # LOG
# LOG_FILE_PATH_KAFKA_REDIS ='D:\\recommend\prodrec\log\kafka_redis_'
# LOG_FILE_PATH_RETURN_ABNORMAL = 'D:\\recommend\prodrec\log\\return_abnormal_'
# LOG_FILE_PATH_RETURN_NORMAL = 'D:\\recommend\prodrec\log\\return_normal_'
# LOG_FILE_PATH_UTIL_REDIS = 'D:\\recommend\prodrec\log\\util_redis_'
# LOG_FILE_PATH_FUNC = 'D:\\recommend\prodrec\log\\func_'
#
#
# # kafka configuration
# KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
# KAFKA_GROUP_ID = 'footInfoProdTest0620'
# KAFKA_PROD_FOOTTOPIC = 'footcom'
#
#
# # redis configuration
# REDIS_HOST = '52.80.137.153'
# REDIS_PORT = 6379
# REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}
#
# # kafka 数据转入redis中的队列名 uuid
# REDIS_KAFKA_LIST = 'kafka_redis_list_data'
# # kafka 数据转入redis中的哈希表名 uuid footdata
# REDIS_KAFKA_HASHSET = 'kafka_redis_hash_data'
#
# # 异常脚数据存入redis的队列名称
# REDIS_LIST_FOOTDATA_EXCEPT = 'redis_list_footdata_except'
# # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
# REDIS_LIST_COMPUTE_RESULT = 'redis_list_compute_result'
#
# # return url
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsgman'





# online
# LOG
# online
LOG_FILE_PATH_KAFKA_REDIS ='/home/ec2-user/zhanghao/log/kafka_redis_'
LOG_FILE_PATH_RETURN_ABNORMAL = '/home/ec2-user/zhanghao/log/return_abnormal_'
LOG_FILE_PATH_RETURN_NORMAL = '/home/ec2-user/zhanghao/log/return_normal_'
LOG_FILE_PATH_UTIL_REDIS = '/home/ec2-user/zhanghao/log/util_redis_'
LOG_FILE_PATH_FUNC = '/home/ec2-user/zhanghao/log/func_'


# kafka configuration
KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
KAFKA_GROUP_ID = 'footInfoProd0620'
KAFKA_PROD_FOOTTOPIC = 'footInfoProd'



# redis configuration
REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
REDIS_PORT = 6379
REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}

# kafka 数据转入redis中的队列名 uuid
REDIS_KAFKA_LIST = 'kafka_redis_list_data'
# kafka 数据转入redis中的哈希表名 uuid footdata
REDIS_KAFKA_HASHSET = 'kafka_redis_hash_data'

# 异常脚数据存入redis的队列名称
REDIS_LIST_FOOTDATA_EXCEPT = 'redis_list_footdata_except'
# 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
REDIS_LIST_COMPUTE_RESULT = 'redis_list_compute_result'


# return url
# RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'

