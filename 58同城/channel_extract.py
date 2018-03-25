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
host_url="http://bj.58.com"

def get_channel_urls(url):
    web_data=requests.get(start_url)
    selector=etree.HTML(web_data)
    xpath_str="//ul[@class='ym-mainmnu']/li[@class='ym-tab']/span[@class='dlb']/a/text"
    content=selector.xpaht(xpath_str)
    print(content)

def main():
    get_channel_urls()

if __name__=='__main__':
    main()














