# 1. kafka 配置
# kafka线上topic
# KAFKA_PROD_FOOTTOPIC = 'footInfoProd'
# KAFKA_PROD_BROKERS = ['54.222.152.174:9092','54.222.195.114:9092','52.80.73.74:9092']
# KAFKA_GROUP_ID = 'footInfoProd1015Test'
# 新地址
KAFKA_PROD_FOOTTOPIC = 'epoque_bigdata_footInfoprod'
KAFKA_PROD_BROKERS = ['10.240.12.26:9092','10.240.251.129:9092','10.240.251.130:9092']
KAFKA_GROUP_ID = 'footInfoProd1015'

# 2. redis配置
# redis线上地址
# 新地址
# REDIS_HOST = '10.240.18.49'
REDIS_HOST = '10.240.117.16'
# REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
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


# 3.返回接口配置
# 线上接口地址
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'
# RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsgman'

# 4. 日志配置
# 日志线上路径
# online
# LOG_FILE_PATH_KAFKA_REDIS ='/home/ec2-user/zhanghao/log/kafka_redis_'
# LOG_FILE_PATH_RETURN_ABNORMAL = '/home/ec2-user/zhanghao/log/return_abnormal_'
# LOG_FILE_PATH_RETURN_NORMAL = '/home/ec2-user/zhanghao/log/return_normal_'
# LOG_FILE_PATH_UTIL_REDIS = '/home/ec2-user/zhanghao/log/util_redis_'
# LOG_FILE_PATH_FUNC = '/home/ec2-user/zhanghao/log/func_'

# 新
LOG_FILE_PATH_KAFKA_REDIS ='/root/log/recommend/kafka_redis_'
LOG_FILE_PATH_RETURN_ABNORMAL = '/root/log/recommend/return_abnormal_'
LOG_FILE_PATH_RETURN_NORMAL = '/root/log/recommend/return_normal_'
LOG_FILE_PATH_UTIL_REDIS = '/root/log/recommend/util_redis_'
LOG_FILE_PATH_FUNC = '/root/log/recommend/func_'