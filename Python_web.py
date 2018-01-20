#!/usr/bin/python
# -*- coding: UTF-8 -*-

import SimpleHTTPServer
import SocketServer
import urlparse
import os
import json


class SETHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        shell_command = ''

        if '?' in self.path:
            query_string = urlparse.unquote(self.path.split('?', 1)[1])
            params = urlparse.parse_qs(query_string)
            client_json = params['json'][0]
            client_data = json.loads(client_json)

            if client_data['request'] == 'courses_by_keywords':
                shell_command = 'python Shnu_course_table.py -k {0} -t json -s'.format(client_data['keywords'].encode('utf-8'))

        p = os.popen(shell_command)

        self.protocal_version = 'HTTP / 1.1'

        self.send_response(200)

        self.send_header("server", "T Engine 假装自己很牛逼")

        self.end_headers()

        self.wfile.write(p.read())

    def stop_server(self):
        self.sorket.close()


PORT = 8081

Handler = SETHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
