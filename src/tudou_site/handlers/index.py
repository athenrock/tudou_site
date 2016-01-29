# /usr/bin/env python
# -*- coding: utf-8 -*-  
# ---------------------------------------
#   程序：   
#   作者：wanghui  
#   日期：16-1-29
#   语言：Python   
#   操作：  
#   功能：
# ---------------------------------------

from tornado import web
from tornado import gen

from tudou_site.handlers.base import SessionBaseHandler


class IndexHandler(SessionBaseHandler):
    @gen.coroutine
    def get(self):
        self.render('index1.html')
        # self.render('index.html')
