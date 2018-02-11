# -*- coding: utf-8 -*-
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://search.jd.com/Search?keyword=三星s7&enc=utf-8&wq=三星s7&pvid=tj0sfuri.v70avo'
req = requests.get(url)
print req.content