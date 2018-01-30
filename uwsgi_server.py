#!/usr/bin/env python
# encoding=utf8

import web
import urlparse
import json
import os
import urllib
import sys
import Function_adapter

urls = (
    '/(.*)', 'myweb'
)

app = web.application(urls, globals())


class myweb:
    def GET(self, name):
        reload(sys)

        sys.setdefaultencoding('utf8')

        full_path = web.ctx.fullpath

        raw = urllib.unquote(full_path).encode('raw_unicode_escape')

        unicode_str = raw.decode()

        call_back_data = '{No Function}'

        if '?' in full_path:
            query_string = urlparse.unquote(unicode_str.split('?', 1)[1])

            params = urlparse.parse_qs(query_string)

            client_json = params['json'][0]

            print client_json.encode('utf-8')

            client_data = json.loads(client_json)

            call_back_data = Function_adapter.run(client_data['request'], client_data['keywords'])

        return call_back_data


application = app.wsgifunc()
