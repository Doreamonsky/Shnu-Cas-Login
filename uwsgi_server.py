#!/usr/bin/env python
# -*- coding:utf-8 -*-
import web
import urlparse
import json
import os

urls = (
    '/(.*)', 'myweb'
)

app = web.application(urls, globals())


class myweb:
    def GET(self, name):
        full_path = web.ctx.fullpath
        shell_command = 'ls'

        if '?' in full_path:
            query_string = urlparse.unquote(full_path.split('?', 1)[1])
            params = urlparse.parse_qs(query_string)
            client_json = params['json'][0]
            client_data = json.loads(client_json)

            if client_data['request'] == 'courses_by_keywords':
                shell_command = 'python Shnu_course_table.py -k {0} -t json -s'.format(
                    client_data['keywords'].encode('utf-8'))

        p = os.popen(shell_command)

        return p.read()


application = app.wsgifunc()
