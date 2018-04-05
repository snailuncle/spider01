from selenium import webdriver
import time
from scrapy.selector import Selector
path=r"D:\spider01\chromedriver.exe"
browser=webdriver.Chrome(executable_path=path)

url="http://125.35.6.80:8080/ftba/itownet/hzp_ba/fw/pz.jsp?processid=20180316153754bjwqv&nid=20180316153754bjwqv"

browser.get(url)
# print(browser.page_source)
title=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h1").text
company=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h3").text
loc=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h6:nth-child(5)").text
component=browser.find_element_by_css_selector("#dzpznr > div:nth-child(3) > ul").text
Specifications=browser.find_element_by_css_selector("#dzpznr > div:nth-child(4) > ul > li:nth-child(1)").text

data={
    'title':title,
    'compant':company,
    'loc':loc,
    'component':component,
    'Specifications':Specifications
}
for key,value in data.items():
    print(key+':'+value)
