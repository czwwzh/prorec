#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
import re
from logging.handlers import TimedRotatingFileHandler


"""
获取日志处理对象
:param appName: 应用程序名
:param logFileName: 日志文件名
:param out: 设置输出端：0：默认控制台，1：输入文件，其他：控制台和文件都输出
:return: 返回日志对象
"""
class Logger(object):
    def __init__(self, appName, logFileName, out=0):
        self.appName = appName
        self.logFileName = logFileName
        self.out = out

    def getLogger(self):
        # 获取logging实例
        logger = logging.getLogger(self.appName)
        # 设置日志级别
        logger.setLevel(logging.INFO)

        # 设置日志处理器
        fh = TimedRotatingFileHandler(
            self.logFileName,
            when="MIDNIGHT",
            backupCount=7)

        # 日志输出到log中配置
        # 日志输出文件名称后缀
        fh.suffix = "%Y-%m-%d.log"
        # 设置日志级别
        fh.setLevel(logging.INFO)
        # 文件回滚后缀匹配
        fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")

        # 日志输出格式
        formatter = logging.Formatter(
            '%(name)s - %(filename)s - %(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(message)s')
        fh.setFormatter(formatter)


        # 日志本地console窗口打印配置  开发调试使用
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        # 为logger添加具体的日志处理器输出端
        if self.out == 1:
            logger.addHandler(fh)
        elif self.out == 0:
            logger.addHandler(ch)
        else:
            logger.addHandler(fh)
            logger.addHandler(ch)
        return logger
