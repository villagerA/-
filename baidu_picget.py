#_*_ coding: utf-8 _*_
import urllib
import requests
import re
import os


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import TimeoutException


# if os.path.exists("d:/demo/python27/pictureget/富士XE3"):
# 	print ('ss')
# else:
# 	print ('no')

content = input("输入想要下载的图片主题：")
dirname = input("输入保存的问价夹得名字：") + "/"
if os.path.exists("d:/demo/python27/pictureget/"+dirname):
	# print ('ss')
	pass
else:
	os.mkdir(dirname)
# try:
# 	os.mkdir(dirname)
# except:
# 	pass
	

baseurl = 'http://image.baidu.com/'
driver = webdriver.Chrome()
driver.get(baseurl)
driver.find_element_by_name("word").send_keys(content)
driver.find_element_by_class_name("s_btn").send_keys(Keys.ENTER)
url = driver.current_url
driver.close()
html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
# 果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个
i = 0
for each in pic_url:
    print(each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print ('[错误]当前图片无法下载')
        continue
    string = dirname + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
# driver.close()

print'\n'.join([''.join([('AndyLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])


print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))
    (lambda s,z,c,n:z 
    if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))2 
    else' 'for x in range(-80,20)])for y in range(-20,20)])