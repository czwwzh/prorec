#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import logging
import re
from logging.handlers import TimedRotatingFileHandler


def get_logger(logFilePath,log_comment):

    logger = logging.getLogger(log_comment)
    logger.setLevel(logging.DEBUG)

    fh = TimedRotatingFileHandler(
        logFilePath,
        when="MIDNIGHT",
        backupCount=7)

    # 日志输出到log中配置
    fh.suffix = "%Y-%m-%d.log"
    fh.setLevel(logging.INFO)
    fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


    # 日志本地console窗口打印配置  开发调试使用
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)

    return logger


