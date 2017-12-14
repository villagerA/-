#_*_ coding: utf-8 _*_
import os
import sys
# import urllib2
import requests
import re
import mysql.connector
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from lxml import etree

# reload(sys)  
# sys.setdefaultencoding('utf8')

# conn = mysql.connector.connect(
#     user = 'root',
#     password = '123456',
#     database = 'news',
#     charset = "utf8")
# cursor = conn.cursor()
# # tablename = raw_input("input the name of the data table you want to save: ")

# cursor.execute("create table if not exists "+tablename+
# #     " (author char(100),emai char(100),title char(255),time char(100),periodical char(100))" )
# cursor.execute("insert into ss(author,email,title,time,periodical")

def request(url):
    headers = {    
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive'
        }
    req = urllib2.Request(url,headers=headers)
    return urllib2.urlopen(req).read()


i = 1
page = 0
url = 'https://www.huxiu.com/'
driver = webdriver.Firefox()
driver.get(url)
# try:
for i in range(10):
	time.sleep(7)
	more = driver.find_element_by_xpath('//*[@id="gs_r gs_or gs_scl"]/div[1]/div[3]')
	
	# thread.sleep(2000)
	# try:
	more.click()
	print("*********************************************************************")
		# except:
			# time.sleep(5)
			# continue
		
		
	# Actions action = new Actions(driver);  
	# acton.moveToElement(more)
	# action.click().perform()
# except:
# 	pass

links = driver.find_elements_by_xpath('//*[@id="index"]/div[1]/div[2]/div')
for i in links:
	try:
		title = i.find_element_by_xpath('div[3]/h2/a').text
		url = i.find_element_by_xpath('div[3]/h2/a').get_attribute('href')
	except:
		title = i.find_element_by_xpath('div[2]/h2/a').text
		url = i.find_element_by_xpath('div[2]/h2/a').get_attribute('href')
	
	print(title)
	print(url)
	print('\n')

	
	

        


