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


def begin(url,tablename):

	driver = webdriver.Chrome() 
	driver.set_page_load_timeout(80)
	driver.get(url)
	periodical = driver.find_element_by_xpath('//*[@id="centerInner"]/div[1]/div[2]/div/a/span').text
	time = driver.find_element_by_xpath('//*[@id="centerInner"]/div[1]/div[2]/p[1]').text
	title = driver.find_element_by_xpath('//*[@id="title0010"]').text
	# try:

		# driver.get(url)
		# driver.set_page_load_timeout(10)
	ag =  driver.find_elements_by_css_selector(".authorName.svAuthor")
	paperdataset = []
	for i in ag:
		if i.text == '':
			continue

		author = i.text
	# print name

		# try:
		i.click()
		# except:
		# 	pass
		emails = driver.find_elements_by_xpath('//*[@id="rightInner"]/div[2]/div/dl/dd')
		for e in emails:
			try:
				email = e.find_element_by_xpath('p/a').text
				if '@' not in email:
					email = ''
				else:
					break
			except:
				email = ''

		if '@' in email:
			print author.encode('GBK', 'ignore')
			print email
			print time
			print periodical
			# print workin
			print ''
		driver.close()

if __name__ == '__main__':
	url = 'http://www.sciencedirect.com/science/article/pii/S0379711217307257'
	tablename= ''
	begintype1(url, tablename)
