#coding:utf-8

import urllib2
import urllib

import json

opener = urllib2.build_opener()
para = {'json':json.dumps({'request':'courses_by_keywords','keywords':'2017,工程管理,1班'})}

print urllib.urlencode(para)

respond = opener.open('https://waroftanks.cn/py/?{0}'.format(urllib.urlencode(para)))

print respond.read()
