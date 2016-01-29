#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tudou_site import settings
import db

kw = {
    "charset": "utf8"
}
db.create_engine(settings.mysql_option['user'], settings.mysql_option['passwd'],
                 settings.mysql_option['db'],
                 settings.mysql_option['host'], settings.mysql_option['port'], **kw)