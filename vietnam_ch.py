#_*_ coding: utf-8 _*_
import os
import sys
import urllib2
import requests
import re
import time
import codecs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from lxml import etree


reload(sys)  
sys.setdefaultencoding('utf8') 

send_headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Connection':'keep-alive'
	}



def getAllLinks(rootlink, cacheUrlFile, pagenum = 20):
	driver = webdriver.Chrome()
	driver.get(rootlink)
	for i in range(pagenum):
		target = driver.find_element_by_id("idviewsmores")
		driver.execute_script("arguments[0].scrollIntoView();", target)
		onc = driver.find_element_by_xpath('//*[@id="idviewsmores"]')
		onc.click()
		print 'Flip page(10s)...'
		time.sleep(10)
	req = html =  driver.page_source
	fw1 = codecs.open(cacheUrlFile, 'a', 'utf-8')
	titles1 = driver.find_elements_by_xpath('//*[@class="clearfix"]')
	urls = []
	for i in titles1:
		try:
			# content = ''
			url = i.find_element_by_xpath('h3/a').get_attribute("href")
			urls.append(url)
			fw1.write(url+'\n')
		except:
			pass


def getLinksFromFile(urlcachefile):
	f = open(urlcachefile)
	links = []
	for line in f.readlines():
		links.append(line.strip())
	return links

def crawlNews(links, targetfilepath):
	fw2 = codecs.open(targetfilepath, 'w', 'utf-8')
	for i in links:
		print i
		r = requests.get(i, headers = send_headers)
		req = str(r.text)
		html = etree.HTML(req)
		cons = html.xpath('//*[@style="font-size:16px;"]/text()')
		title = html.xpath('//*[@class="clearfix fon4"]/text()')[0].strip()
		# print title
		fw2.write(title+'\n')
		content = ''
		for i in cons:
			try:		
				if '越通社记者' in i:
					continue
				if '越通社资料' in i:
					continue
				# print i.strip()
				content =content + i.strip()
			except:
				pass
		fw2.write(content+'\n')
		print 'get！'
		



if __name__ == '__main__':
	rootlink = 'https://vietnam.vnanet.vn/chinese/%E8%A7%86%E7%82%B9/77.vnp'
	cacheUrlFile = 'url_ch.txt'
	pagenum = int(raw_input("Enter the number of pages flipped:"))
	print "1.try to get links..."
	links = getAllLinks(rootlink, cacheUrlFile,pagenum)  # the first step
	print "links get!!"
	print "2.open links..."
	links = getLinksFromFile(cacheUrlFile) # 
	print "3.craw links..."
	crawlNews(links, 'con_ch.txt')
	print "finish"

