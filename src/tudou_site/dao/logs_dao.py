# /usr/bin/env python
# -*- coding: utf-8 -*-  
# ---------------------------------------
#   程序：   
#   作者：wanghui  
#   日期：16-1-6
#   语言：Python   
#   操作：  
#   功能： 日志管理
# ---------------------------------------

from tornado import gen
import db


@gen.coroutine
def insert(log):
    db.insert("logs", **log)


@gen.coroutine
def find_logs_for_table(kwargs, start=0, size=10):
    sql_count = " select count(*) from logs "
    sql = " select * from `logs` "

    if kwargs:
        where = " where "
        if kwargs.get('created'):
            s = kwargs.get('created').get("start")
            e = kwargs.get('created').get("end")
            kwargs.pop('created')
            where += "created > '%s' and created< '%s' " % (s, e)
        where += ' and '.join(["`%s`=%s" % (k, v) for k, v in kwargs])
        sql_count += where
        sql += where
    sql += ' order by created desc limit ?,?; '
    count = db.select_int(sql_count)
    logs = db.select(sql, start, size)

    result = {
        "count": count,
        "data": logs
    }
    raise gen.Return(result)
