#!/bin/bash
#source /home/ec2-user/virtualenv36/bin/activate
source /root/virtualenv36/bin/activate
nohup python -u /root/projects/recommend/prodrec/data_convert_cache/kafka_redis.py >/dev/null 2>&1 &
nohup python -u /root/projects/recommend/prodrec/data_convert_cache/return_abnormal_data.py >/dev/null 2>&1 &
nohup python -u /root/projects/recommend/prodrec/data_convert_cache/return_normal_data.py >/dev/null 2>&1 &

