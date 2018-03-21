from selenium import webdriver
import time
from scrapy.selector import Selector
path=r"D:\spider01\chromedriver.exe"
# browser=webdriver.Chrome(executable_path=path)

url="http://image.baidu.com/search/index?tn=baiduimage&word=%E7%BE%8E%E5%A5%B3"

# browser.get(url)
# time.sleep(5)
# print(browser.page_source)
# title=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h1").text
# company=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h3").text
# loc=browser.find_element_by_css_selector("div.dzpznr > div.dzpztypes > h6:nth-child(5)").text
# component=browser.find_element_by_css_selector("#dzpznr > div:nth-child(3) > ul").text
# Specifications=browser.find_element_by_css_selector("#dzpznr > div:nth-child(4) > ul > li:nth-child(1)").text

# data={
#     'title':title,
#     'compant':company,
#     'loc':loc,
#     'component':component,
#     'Specifications':Specifications
# }
# for key,value in data.items():
#     print(key+':'+value)
#不加载图片
chrome_opt=webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_opt.add_experimental_option("prefs",prefs)
browser=webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)
browser.get(url)
time.sleep(3)
for i in range(3):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    time.sleep(3)

time.sleep(3)
browser.quit()


