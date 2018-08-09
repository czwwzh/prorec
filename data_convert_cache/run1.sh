#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/data_convert_cache/return_abnormal_data.py >/dev/null 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/data_convert_cache/return_abnormal_data.py >/dev/null 2>&1 &

nohup python -u /home/ec2-user/zhanghao/prodrec/data_convert_cache/return_normal_data.py >/dev/null 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/data_convert_cache/return_normal_data.py >/dev/null 2>&1 &
