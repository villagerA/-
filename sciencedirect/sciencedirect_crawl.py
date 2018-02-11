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

	# 
	# req = requests.get(url)
	# h5 = etree.HTML(req.content)
	driver = webdriver.Chrome()
	driver.get(url)
	# print (driver.page_source)

	periodical = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[1]/div[2]/h2/span/a')[0].text
	time = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[1]/div[2]/div[1]/span')[0].text
	title = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/h1/span')[0].text
	# try:

		# driver.get(url)
		# driver.set_page_load_timeout(10)
	ag =  driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[2]/div/div/div/a')
	paperdataset = []
	for i in ag:
		# if i.text == '':
		# 	continue

		author = i.text
	# print name

		# try:
		i.click()
		# except:
		# 	pass
		emails = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[3]/div/div/div[2]/div')
		for e in emails:
			try:
				email = e.find_element_by_xpath('a').text
				if '@' not in email:
					email = ''
				else:
					bresak
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
	url = 'https://www.sciencedirect.com/science/article/pii/S2212095516300621'
	tablename= ''
	begin(url, tablename)