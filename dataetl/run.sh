#!/bin/bash
source /root/virtualenv36/bin/activate
nohup python -u /root/projects/recommend/prodrec/dataetl/etl.py >/dev/null 2>&1 &
