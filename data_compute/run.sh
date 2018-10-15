#!/bin/bash
source /root/virtualenv36/bin/activate
nohup python -u /root/projects/recommend/prodrec/data_compute/compute.py >/dev/null 2>&1 &
