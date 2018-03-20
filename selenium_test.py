from selenium import webdriver
import time
from scrapy.selector import Selector
path=r"D:\spider01\chromedriver.exe"
browser=webdriver.Chrome(executable_path=path)

url="https://detail.tmall.com/item.htm?id=536517932355&ali_refid=a3_430583_1006:1122061755:N:Python:048e415c35bfcb466dbc4f4d35bf7a7a&ali_trackid=1_048e415c35bfcb466dbc4f4d35bf7a7a&spm=a230r.1.14.1&sku_properties=14829532:72110507"

browser.get(url)
print(browser.page_source)
t_selector=Selector(text=browser.page_source)
info=t_selector.css(".poptip-content .iconfont::text").extract()
print(info)

time.sleep(5)
browser.quit()
