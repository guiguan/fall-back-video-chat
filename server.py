#!/usr/bin/python
#
# server
#    python server.py
#
# browser
#    https://0.0.0.0:4443
#
# @Author: Guan Gui <guiguan>
# @Date:   2016-04-27T11:00:48+10:00
# @Email:  root@guiguan.net
# @Last modified by:   guiguan
# @Last modified time: 2016-04-28T01:49:41+10:00



import BaseHTTPServer
import SimpleHTTPServer
import ssl
import os

# os.system("openssl req -new -keyout server.pem -out server.pem -x509 -days 365 -nodes -subj '/CN=www.pubnub.com/O=PubNub/C=US'")
httpd = BaseHTTPServer.HTTPServer( ( '0.0.0.0', 4443 ), SimpleHTTPServer.SimpleHTTPRequestHandler )
httpd.socket = ssl.wrap_socket( httpd.socket, certfile='./server.pem', server_side=True )
httpd.serve_forever()
