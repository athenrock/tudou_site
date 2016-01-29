#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from tornado import gen

from tudou_site.dao import logs_dao

LOGIN = "登录"
LOGOUT = "退出"
FORGET = "忘记密码"
UPSET = "修改"


@gen.coroutine
def insert_logs(log):
    log['created'] = datetime.now()
    yield logs_dao.insert(log)


@gen.coroutine
def find_logs_for_table(kwargs, start=0, size=10):
    result = yield logs_dao.find_logs_for_table(kwargs, start, size)
    raise gen.Return(result)
