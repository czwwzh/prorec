#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author: zhanghao
@contact: zhanghao@epoque.shoes
@file: configuration_test.py
@time: 2018/5/29/029  8:02
"""

# sku recommend dataetl and compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_CHARSET = 'utf8mb4'
# prod db
# RECOMMEND_DB_NAME = 'shop_sku_recommend'
# test db
RECOMMEND_DB_NAME = 'bdp_products'

FOOT_LAST_ETL_TABLE = 'foot_last_etl'
FOOT_SCAN_TABLE = 'foot_scan'
FOOT_REPEAT_TABLE = 'foot_repeat'
