#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from kafka import KafkaConsumer

consumer = KafkaConsumer('footcom',
                         group_id='comoute1',
                         bootstrap_servers=['54.222.152.174:9092', '54.222.195.114:9092', '52.80.73.74:9092'])
if __name__ == '__main__':
    count = 0
    for message in consumer:
        count += 1
        print(count)
        # print(type(message.key))
        # key = message.key
        # value = message.value
        # print(type(key))
        # print(type(value))
        #
        # print(key)
        # print(value)
        # value =  demjson.decode(message.value)
        # print(value)
        # print(message.value.decode())
        # json.dumps(message.value.decode())
        # time.sleep(1)