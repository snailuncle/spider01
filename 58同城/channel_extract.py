#转转,更专业的二手平台
# url="http://bj.58.com/sale.shtml"
# html=requests.get(url).text
# # print(html)
# selector=etree.HTML(html)
# xpath_str="//li[@class='scitem scitemimage']/div[@class='simgbody simgh cl']/a[@class='simgtitle']/text()"
# content=selector.xpath(xpath_str)
# # print(content)
# for each in content:
#     print(each)
from bs4 import BeautifulSoup
import json
import requests
from lxml import etree
import sys
import re
import time

start_url="http://bj.58.com/sale.shtml"
url_host="http://bj.58.com"

def get_channel_urls(url):
    web_data=requests.get(start_url)
    # web_data.encoding=web_data.apparent_encoding
    # print(web_data.encoding)
    web_data=web_data.text
    # with open('58同城/channel_link.txt','w',encoding='utf-8') as f:
    #     f.write(web_data)
    selector=etree.HTML(web_data)
    xpath_str="//ul[@class='ym-mainmnu']/li[@class='ym-tab']/span[@class='dlb']/a/@href"
    links=selector.xpath(xpath_str)
    for link in links:
        page_url=url_host+link
        print(page_url)

def main():
    get_channel_urls(start_url)

if __name__=='__main__':
    main()
# 所有频道链接
channel_list="""
http://bj.58.com/shouji/
http://bj.58.com/tongxunyw/
http://bj.58.com/danche/
http://bj.58.com/diandongche/
http://bj.58.com/diannao/
http://bj.58.com/shuma/
http://bj.58.com/jiadian/
http://bj.58.com/ershoujiaju/
http://bj.58.com/yingyou/
http://bj.58.com/fushi/
http://bj.58.com/meirong/
http://bj.58.com/yishu/
http://bj.58.com/tushu/
http://bj.58.com/wenti/
http://bj.58.com/bangong/
http://bj.58.com/shebei.shtml
http://bj.58.com/chengren/
"""












