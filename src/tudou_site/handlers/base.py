#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen

try:
    import Cookie  # py2
except ImportError:
    import http.cookies as Cookie  # py3

try:
    import urlparse  # py2
except ImportError:
    import urllib.parse as urlparse  # py3

try:
    from urllib import urlencode  # py2
except ImportError:
    from urllib.parse import urlencode  # py3

from tornado.escape import utf8
from tornado.util import unicode_type

from tudou_site.auth import session
from tudou_site.utils import encoder

from tudou_site.services import logs_service


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def write(self, chunk):
        if self._finished:
            raise RuntimeError("Cannot write() after finish().  May be caused "
                               "by using async operations without the "
                               "@asynchronous decorator.")
        if not isinstance(chunk, (bytes, unicode_type, dict)):
            raise TypeError("write() only accepts bytes, unicode, and dict objects")
        if isinstance(chunk, dict):
            chunk = encoder.json_encode(chunk)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)


class SessionBaseHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def __init__(self, *argc, **argkw):
        super(SessionBaseHandler, self).__init__(*argc, **argkw)
        self._session = session.Session(self.application.session_manager, self)
        self.user_menus_data = None
        # self._logger = logger

    @tornado.gen.coroutine
    def set_current_user(self, user_info):
        #user_menus_data = yield menus_service.get_user_menus(user_info.get('id'))
        #user_info['menus_data'] = user_menus_data
        self._session["user_info"] = user_info
        self._session.save()

    def get_current_user(self):
        """
        覆盖父类的方法,用于系统的用户验证
        """
        return self._session.get("user_info")

    @tornado.gen.coroutine
    def prepare(self):
        user = self.get_current_user()
        # if user:
        #     user_roots = yield menus_service.get_norelos(user.get('id'))
        #     for root in user_roots:
        #         if self.check_href_roles(root.get('href')):
        #             self.redirect('/')

    def check_href_roles(self, href):
        if self.request.path.lower() == href.lower():
            return True

        return False

    @tornado.gen.coroutine
    def logs(self, content, type=logs_service.UPSET):
        '''
        @:type logs_service  LOGIN ="登录"  LOGOUT = "注销" UPSET = "修改/维护"
        '''

        logs = {
            "type": type,
            "content": content,
            "ip": self.request.remote_ip,
            "operator": self.current_user.get("name", "系统")
        }
        yield logs_service.insert_logs(logs)
