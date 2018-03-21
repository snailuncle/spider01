from selenium import webdriver
import time
from scrapy.selector import Selector
path=r"D:\phantomjs\bin\phantomjs.exe"
url="https://detail.tmall.com/item.htm?spm=a230r.1.14.40.390b4dceAZ23ip&id=564090286201&ns=1&abbucket=17"
browser=webdriver.PhantomJS(executable_path=path)
browser.get(url)
print(browser.page_source)
browser.quit()
