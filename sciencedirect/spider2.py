#_*_ coding: utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# chrome_options = Options()
# chrome_options.add_argument("--headless")

def begin(url,tablename):
	driver = webdriver.Chrome()
	driver.set_page_load_timeout(200)
	driver.get(url)

	periodical = driver.find_element_by_xpath('//*[@id="publication-title"]/a').text
	time2 = driver.find_element_by_xpath('//*[@id="publication"]/div[2]/div[1]').text
	title = driver.find_element_by_xpath('//*[@class="author-group"]/a/span').text
	print("title:" + title)
	print("pubdate: " + time2)
	print("periodical anme" + periodical)
	ag = driver.find_elements_by_xpath('//*[@id="author-group"]/a')
	for i in ag:
		# try:
		i.click()
		sur = i.find_element_by_xpath('//*[@id="workspace-author"]/div[1]/span[1]').text
		giv = i.find_element_by_xpath('//*[@id="workspace-author"]/div[1]/span[2]').text
		name = sur + ' ' + giv
		time.sleep(2)
		email = ""
		emails = driver.find_elements_by_xpath('//*[@id="workspace-author"]/div')
		for j in emails:
			t = j.text
			if not t:
				t = j.find_element_by_xpath('//*').text
			if '@' in t:
				email = t
				break
		if email:
			print('name:' + name)
			print("title:" + title)
			print("pubdate: " + time2)
			print("periodical anme" + periodical)
			print("email:" + email)
			print('----' * 10)

		else:
			print('----' * 10)
			print('name:' + name)
			print("title:" + title)
			print("pubdate: " + time2)
			print("periodical anme" + periodical)
			print("no email")
			print('----' * 10)
	driver.close()

if __name__ == '__main__':
	url = 'https://www.sciencedirect.com/science/article/pii/S0040402018312298'
	tablename= ''
	begin(url, tablename)
