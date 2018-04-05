from selenium import webdriver
import time
from scrapy.selector import Selector
path=r"D:\spider01\chromedriver.exe"
browser=webdriver.Chrome(executable_path=path)

url="https://www.zhihu.com/signup"

browser.get(url)
# print(browser.page_source)
#点击登录按钮,切换到登录界面
info=browser.find_element_by_css_selector(".SignContainer-switch span[data-reactid='94']")
print(info.text)
print(dir(info))
info.click()
time.sleep(2)

#输入账号密码
user='123'
password='123'

info=browser.find_element_by_css_selector("div.SignFlow-accountInput.Input-wrapper > input").send_keys(user)
time.sleep(1)
info=browser.find_element_by_css_selector("div.SignContainer-inner > div.Login-content > form > div.SignFlow-password > div > div.Input-wrapper > input").send_keys(password)
time.sleep(1)
info=browser.find_element_by_css_selector("div.SignContainer-inner > div.Login-content > form > button").click()

# 5秒后关闭浏览器
time.sleep(5)
browser.quit()
