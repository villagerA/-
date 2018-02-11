# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['jd.com']
    start_urls= []
    for i in range(1, 7, 2):
        url = 'http://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9Fs8&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=\
        1&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page='+str(i)+'&s='+str(60*(i-1)+1)+'&click=0'
        start_urls.append(url)
    # start_urls = ['http://search.jd.com/Search?keyword=三星s7&enc=utf-8&wq=三星s7&pvid=tj0sfuri.v70avo']
                  # 'http://search.jd.com/Search?keyword=三星s8&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=1&ev=exbrand_三星（SAMSUNG）%5E&page=5&s=121&click=0'
                  # 'http://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9Fs8&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=1&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page=7&s=181&click=0'
                  # 'http://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9Fs8&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=1&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page=9&s=241&click=0'
    def parse(self, response):
        # print response.body
        selector = scrapy.Selector(response)
        links = selector.xpath('//*[@id="J_goodsList"]/ul/li')
        for i in links:
            link = 'http:'+i.xpath('div/div[1]/a/@href').extract()[0]
            print link
        print "*"*40