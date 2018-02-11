#_*_ coding: utf-8 _*_
import os
import sys
import urllib2
import requests
import re
import time
import codecs
import mysql.connector
import xml.etree.cElementTree as ET 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from lxml import etree




reload(sys)  
sys.setdefaultencoding('utf8')

conn = mysql.connector.connect(
    user = 'root',
    password = '123456',
    database = 'allin',
    charset = "utf8")
cursor = conn.cursor()

send_headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Connection':'keep-alive'
	}



def getAllLinks(rootlink):
	r = requests.get(rootlink, headers = send_headers)
	req =  str(r.text)
	h5 = etree.HTML(req)
	links = h5.xpath('//*[@id="JournalInfor_UpdatePanel1"]/div[2]/ul')
	for i in links:
		# link =  i.xpath('p[1]/a')[0].attrib['href']
		try:
			link = i.xpath('p[3]/a[4]')[0].attrib['href']
			url = 'http:'+link
			print url
			try:
				getemail(url)
			except:
				pass
			time.sleep(3)
		except:
			pass


def getemail(url):
	r = requests.get(url, headers = send_headers)
	req =  str(r.text)
	# 获取xml文件
	page=etree.fromstring(req)

	# print page[0][1][3][0].text.strip()
	# print page[0][1][7][0][0].text
	title = page.getiterator("article-title")
	for node in title:
		title0 =  node.text.strip()
		print title0
	email = page.getiterator("email")
	# email = ''
	for node in email:
		email0 =  node.text
		print email0
		cursor.execute("insert into www_scirp_org_f (title,email) values (%s,%s)",[title0,email0])# last:email_geology_2015
		conn.commit()
	# print email
	



if __name__ == '__main__':
	for i in range(4,20):
		url = 'http://www.scirp.org/Journal/AllArticle.aspx?JournalID=610&page='+str(i)
		print url
		getAllLinks(url)
		time.sleep(10)
		# break

	url = 'http://www.scirp.org/Journal/AllArticle.aspx?JournalID=609'
	# # url = 'http://www.runoob.com/mysql/mysql-order-by.html'
	getAllLinks(url)
	# url = 'http://www.scirp.org/Journal/PaperInformation.aspx?PaperID=78951'
	# url = 'http://file.scirp.org/xml/78951.xml'
	# getemail(url)
