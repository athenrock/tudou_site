# /usr/bin/env python
# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：   
#   作者：wanghui  
#   日期：16-1-29
#   语言：Python   
#   操作：  
#   功能：
#---------------------------------------  




import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
from tornado.options import define, options

from tudou_site import settings
from tudou_site.urls import admin
from tudou_site.auth import session

# from spk_site.modules import modules

define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # settings.app['ui_modules'] = modules.ui_modules
        super(Application, self).__init__(admin.handlers, **settings.app)
        self.session_manager = session.SessionManager(
            settings.app["session_secret"],
            settings.app["session_timeout"])


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print('exit')


if __name__ == "__main__":
    print '---------------'
    main()