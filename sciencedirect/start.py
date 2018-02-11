
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
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
import spider1
from bs4 import BeautifulSoup
from lxml import etree


def begin(url):
	driver = webdriver.Chrome()
	print url
	driver.get(url)

	urls = driver.find_elements_by_xpath('//*[@id="main_content"]/main/div[1]/div[2]/div[2]/ol/li')
	num = 0									
	for i in urls:
		try:
                        print num
                        num= num+1
			url = i.find_element_by_xpath('div/div/h2/a').get_attribute("href")
			print url
			spider1.begin(url,'')
			break
		except:
			pass
	nexturl = 'http://www.sciencedirect.com/search'+driver.find_element_by_xpath('//*[@id="main_content"]/main/div[1]/div[2]/div[3]/div[2]/ol/li[2]/a').get_attribute("href")#.split('http://www.sciencedirect.com/')[1]
	print nexturl
	#begin(nexturl)
	driver.close()
	
	# num = num+1

if __name__ == '__main__':
	url = "http://www.sciencedirect.com"
	content = raw_input("Please enter what you want to search for: ")
	driver = webdriver.Chrome()
	driver.get(url)
	driver.find_element_by_name("qs").send_keys(content)
	driver.find_element_by_xpath('//*[@type="submit"]').send_keys(Keys.ENTER)
	time.sleep(1)
	current_url = driver.current_url
	driver.close()
	begin(current_url)

# for i in range(10):
# 	url2 = current_url+"&years="+str(year)
# 	urlset.append(url2)
# 	year = year-1
# 	print url2
# 	if year == 2009:
# 		break

# 	for j in range(2):
# 		id = str(index)
# 		newurl = url2+'&offset='+id
# 		# print newurl
# 		urlset.append(newurl)
# 		# print urlset[i]
# 		index += 25
# 	num	= 1
# 	for url in urlset:
# 		# http://www.sciencedirect.com/search?qs=Wastewater+Treatment&authors=&pub=&volume=&issue=&page=&origin=home&zone=qSearch&years=2018
# 		# http://www.sciencedirect.com/search?qs=Wastewater+Treatment&authors=&pub=&volume=&issue=&page=&origin=home&zone=qSearch&years=2018
# 		html = request(url)
# 		# print html
# 		relink = 'getAccessLink":"(http://www.sciencedirect.com/science/article/pii/S.*?)","downloadLink"'
# 	# <a href="http://www.sciencedirect.com/science/article/pii/S0269749117304542" class="result-list-title-link u-font-serif text-s" 

# 		mypage_Info = re.findall(relink,html)
# 		# print mypage_Info
# 		# paperdataset = []

# 		for url in mypage_Info:
# 			print url
# 	print "-----------------------------------------------------------------------"
# 	urlset = []
# 	index =25
	# 		try:
	# 			html = request(url) 
	# 		except:
	# 			continue
	# 		relink0 = '<h1 class="svTitle" id=".*?">(.*?)<.*?/h1>.*?'
	# 		if re.findall(relink0,html):
	# 			print num
	# 			try:
	# 				spider1.begintype1(url,tablename)
	# 				time.sleep(2)
	# 			except:
	# 				# time.sleep(5)
	# 				pass

	# 		else:
	# 			print num
	# 			try:
	# 				spider2.begintype1(url,tablename)
	# 				time.sleep(2)
	# 			except:
	# 				#
	# 				pass
				
	# 		num = num + 1
