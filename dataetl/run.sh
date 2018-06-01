#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/transfer.py &
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/read.py &