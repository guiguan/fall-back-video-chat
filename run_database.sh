#!/bin/bash
#
# @Author: Guan Gui <guiguan>
# @Date:   2016-04-27T12:51:37+10:00
# @Email:  root@guiguan.net
# @Last modified by:   guiguan
# @Last modified time: 2016-04-27T12:54:31+10:00



pouchdb-server -o 0.0.0.0 -p 15984 -d database -c database/config.json
