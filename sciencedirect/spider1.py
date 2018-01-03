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
import spider2
# from bs4 import BeautifulSoup
# from lxml import etree
# from pyquery import PyQuery as pq

reload(sys)  
sys.setdefaultencoding('utf8') #解决插入数据库时编码的问题：ascii' codec can't encode characters...

# conn = mysql.connector.connect(
# 	user = 'root',
# 	password = '123456',
# 	database = 'hahaha',
# 	charset = "utf8")
# cursor = conn.cursor()

def request(url):
	send_headers = {
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    	'Connection':'keep-alive'
	}
    
  
	req = urllib2.Request(url,headers=send_headers)
	return urllib2.urlopen(req).read()


def begin(url,tablename):
	driver = webdriver.Chrome() 
	driver.set_page_load_timeout(80)
	driver.get(url)
	try:
		time = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[1]/div[2]/div/span').text
		title = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/h1/span').text
		periodical = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[1]/div[2]/h2/span/a').text
		                                    
		ag =  driver.find_elements_by_css_selector(".author.size-m.workspace-trigger")
		for i in ag:
		
			# title = re.findall(relink,html)
			# print title
			given_name = ''
			try:
				given_name = i.find_element_by_css_selector(".text.given-name").text
				surname =  i.find_element_by_css_selector(".text.surname").text
				author = given_name+' '+surname
			except:
				author = ''
			
			# print author
			ActionChains(driver).move_to_element(i).perform()
			try:
				i.click()
			except:
				pass
			email = ''
			workin = ''
			emails = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/section/div/div[3]/div/div/div[2]/div')
			for e in emails:
				try:
					email = e.find_element_by_xpath('a').text
					if '@' not in email:
						email = ''
					else:
						break
				except:
					email = ''
				try:
					workin = e.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div[3]/div/div/div[2]/div[2]/span').text
				except:
					workin = ''

			if '@' in email:
				print author.encode('GBK', 'ignore')
				print email
				print time
				print periodical
				print workin
			print ''
			# driver.close()
		driver.close()
		# except:
		# 	driver.close()
	except:
		driver.close()
		spider2.begin(url,tablename)

if __name__ == '__main__':
	# url = 'http://www.sciencedirect.com/science/article/pii/S0939362517300262'
	url = 'http://www.sciencedirect.com/science/article/pii/S0379711217307257'
	tablename= ''
	begin(url, tablename)
