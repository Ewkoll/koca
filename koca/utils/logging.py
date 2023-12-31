#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description:  获取日志信息
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:29:55
LastEditTime: 2023-09-17 23:30:36
'''
from __future__ import absolute_import
import os
from logging import getLogger, Formatter, StreamHandler, FileHandler

__all__ = [
    "get_logger",
    "create_logger",
]

DEFAULT_LOGGER_PATH = "log"
DEFAULT_LOGGER_NAME = "app"
DEFAULT_FORMAT = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
logger = None


def get_logger(name=DEFAULT_LOGGER_NAME, path=DEFAULT_LOGGER_PATH, _format=DEFAULT_FORMAT):
    '''
    @description: 获取默认的日志输出。
    @return: 
    '''
    global logger

    if logger:
        return logger
    else:
        logger = create_logger(name, path, _format)
        return logger


def create_logger(name=None, path=None, _format=None):
    '''
    @description: 创建默认的日志输出。
    @return: 
    '''
    logger_name = name or DEFAULT_LOGGER_NAME
    logger = getLogger(logger_name)
    logger.propagate = False

    if not logger.handlers:
        formatter = Formatter(fmt=_format or DEFAULT_FORMAT)

        if path:
            if not os.path.exists(path):
                os.makedirs(path)
            handler = FileHandler(path + "/" + logger_name + ".log")
        else:
            handler = StreamHandler()

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
