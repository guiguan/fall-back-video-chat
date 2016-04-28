#!/bin/bash
#
# @Author: Guan Gui <root>
# @Date:   2016-04-28T09:19:05+10:00
# @Email:  root@guiguan.net
# @Last modified by:   root
# @Last modified time: 2016-04-28T09:22:26+10:00



http-server -p 9000 --cors -P http://localhost:15984 -S -C server-ssl.crt -K server-ssl.key
