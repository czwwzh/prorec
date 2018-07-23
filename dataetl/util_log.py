#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import logging
import re
from logging.handlers import TimedRotatingFileHandler


# 日志工具，按天存储  0点回滚
# 入参： 日志路径和日志打印名称
# 2018-07-22 22:52:47,942 - model-compute-log - INFO - 8.model data_compute result send to redis time:  2018-07-22 22:52:47
def get_logger(logFilePath,log_comment):
    # 获取日志实例
    logger = logging.getLogger(log_comment)
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 设置日志处理器
    fh = TimedRotatingFileHandler(
        logFilePath,
        when="MIDNIGHT",
        backupCount=7)


    # 日志输出到log中配置
    # 输出文件名称后缀
    fh.suffix = "%Y-%m-%d.log"
    # 设置日志级别
    fh.setLevel(logging.INFO)
    # 文件回滚后缀匹配
    fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")

    # 日志输出格式
    formatter = logging.Formatter('%(name)s - %(filename)s - %(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


    # 日志本地console窗口打印配置  开发调试使用
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)

    return logger

