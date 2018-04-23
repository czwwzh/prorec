#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/transfer.py> /home/ec2-user/zhanghao/prodrec/log/dataetl/log/transfer_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/read.py> /home/ec2-user/zhanghao/prodrec/log/dataetl/log/read_`date "+%Y-%m-%d"`.log 2>&1 &