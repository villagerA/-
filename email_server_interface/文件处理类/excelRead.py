#_*_ coding: utf-8 _*_
import os
import sys
import urllib2
import requests
import re
import mysql.connector
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from lxml import etree
# from pyquery import PyQuery as pq

reload(sys)  
sys.setdefaultencoding('utf8') #解决插入数据库时编码的问题：ascii' codec can't encode characters...


import xlrd

fname = fname = raw_input('输入文件名确保文件在当前目录，以.xls为后缀:')
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
	sh = bk.sheet_by_name("Sheet1")
except:
	print "no sheet in %s named Sheet1" % fname

nrows = sh.nrows
ncols = sh.ncols

row_list = []
#获取各行数据
str1= '#!/bin/bash (echo "Content-Type: text/html";cat mail.txt)|/usr/sbin/sendmail'
for i in range(1,nrows):
	row_data = sh.row_values(i)
	str1 = str1+' -c '+row_data[1]
print (str1)
	