#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from datetime import datetime, date, timedelta


class DateTimeEncoder(json.JSONEncoder):
    time_format = '%Y-%m-%d %H:%M:%S'
    date_format = '%Y-%m-%d'

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(self.time_format)
        elif isinstance(obj, date):
            return obj.strftime(self.date_format)
        elif isinstance(obj, timedelta):
            return (datetime.min + obj).time().strftime(self.time_format)
        else:
            return super(DateTimeEncoder, self).default(obj)


# The fact that json_encode wraps json.dumps is an implementation detail.
# Please see https://github.com/tornadoweb/tornado/pull/706
# before sending a pull request that adds **kwargs to this function.
def json_encode(value):
    """JSON-encodes the given Python object."""
    # JSON permits but does not require forward slashes to be escaped.
    # This is useful when json data is emitted in a <script> tag
    # in HTML, as it prevents </script> tags from prematurely terminating
    # the javscript.  Some json libraries do this escaping by default,
    # although python's standard library does not, so we do it here.
    # http://stackoverflow.com/questions/1580647/json-why-are-forward-slashes-escaped
    return json.dumps(value, cls=DateTimeEncoder).replace("</", "<\\/")
