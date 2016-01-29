#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tudou_site.handlers import index

handlers = [
    (r"/", index.IndexHandler),
    (r"/index", index.IndexHandler)

]
