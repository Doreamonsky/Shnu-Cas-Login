#!/usr/bin/env python
# encoding=utf8

import web
import urlparse
import json
import os
import urllib
import sys


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

        shell_command = 'ls'

        if '?' in full_path:
            query_string = urlparse.unquote(unicode_str.split('?', 1)[1])

            params = urlparse.parse_qs(query_string)

            client_json = params['json'][0]

            print client_json.encode('utf-8')

            client_data = json.loads(client_json)

            if client_data['request'] == 'courses_by_keywords':
                shell_command = 'python Shnu_course_table.py -k {0} -t json -s'.format(client_data['keywords'].encode('utf-8'))
            if client_data['request'] == 'courses_by_classroom_keywords':
                shell_command = 'python Shnu_classroom.py -k {0}'.format(client_data['keywords'].encode('utf-8'))
            if client_data['request'] == 'courses_by_id':
                shell_command = 'python Shnu_course_table_by_id.py -k {0}'.format(client_data['keywords'].encode('utf-8'))
        p = os.popen(shell_command)



        return p.read()


application = app.wsgifunc()
