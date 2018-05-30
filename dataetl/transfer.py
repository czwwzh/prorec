#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from kafka import KafkaConsumer



# local
from dataetl.redisutil import Redis_db as rds
from dataetl.dataetlconfiguration import *

# online
# from redisutil import Redis_db as rds
# from dataetlconfiguration import *

consumer = KafkaConsumer(KAFKA_PROD_FOOTTOPIC,
                         group_id=KAFKA_GROUP_ID,
                         bootstrap_servers=KAFKA_PROD_BROKERS)
my_rds = rds('recommend_data_msg')
for message in consumer:
    import traceback
    try:
        key = message.key.decode()
        sourcedata = message.value.decode()
        import json
        # a = json.loads(sourcedata)
        # data = key + "_" + sourcedata
        my_rds.SetData(key,sourcedata)
        my_rds.RpushData(key)
        print(type(key))
        print(key)
        print(type(sourcedata))
        print(sourcedata)
        # json.loads(sourcedata)
    except:
        traceback.print_exc()
        pass

