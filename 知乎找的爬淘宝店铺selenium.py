from selenium import webdriver   
from bs4 import BeautifulSoup  
import random  
import re  
import time  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep



Infolist=[]  
  
def init():     
    firefox_login=webdriver.Chrome()   #构造模拟浏览器  
    firefox_login.get('https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F') #淘宝登录页面  
    firefox_login.maximize_window()#窗口最大化，可有可无，看情况  
    return firefox_login  
      
def login(firefox_login):      
    #输入账户密码  
    #我请求的页面的账户输入框的'id'是username和密码输入框的'name'是password  
    firefox_login.find_element_by_id('J_Quick2Static').click() 
    firefox_login.find_element_by_id('TPL_username_1').clear()  
    firefox_login.find_element_by_id('TPL_username_1').send_keys(u'123456789@qq.com')  
    firefox_login.find_element_by_id('TPL_password_1').clear()  
    firefox_login.find_element_by_id('TPL_password_1').send_keys(u'123456789')  
    time.sleep(1)
    #拖动滑块



    dragger=firefox_login.find_element_by_id('nc_1_n1z')
    # ActionChains(firefox_login).drag_and_drop_by_offset(dragger,280,0).perform()
    # #等待JS认证运行,如果不等待容易报错
    # time.sleep(3)


    action=ActionChains(firefox_login)  
    action.click_and_hold(dragger).perform()
    for index in range(150):
        try:
            action.move_by_offset(20, 0).perform() #平行移动鼠标
            # 移动了两个像素  index
        except UnexpectedAlertPresentException:
            break
        action.reset_actions()
        sleep(0.001)  #等待停顿时间
    success_text = firefox_login.switch_to.alert.text
    print(success_text)
    sleep(1)

# dragger = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

# action = ActionChains(driver)

# action.click_and_hold(dragger).perform()  #鼠标左键按下不放

# for index in range(200):
#     try:
#         action.move_by_offset(2, 0).perform() #平行移动鼠标
#     except UnexpectedAlertPresentException:
#         break
#     action.reset_actions()
#     sleep(0.1)  #等待停顿时间


# # 打印警告框提示
# success_text = driver.switch_to.alert.text
# print(success_text)

# sleep(5)

# driver.quit()












    firefox_login.find_element_by_id('J_SubmitStatic').click()  
    time.sleep(random.randint(2,5))  
    firefox_login.find_element_by_id('q').send_keys(u'代码之美')  
    firefox_login.find_element_by_class_name('btn-search').click()  
    return firefox_login  
def ObtainHtml(firefox_login):  
      
    data=firefox_login.page_source  
    soup = BeautifulSoup(data,'lxml')   
    comments=soup.find_all("div", class_="ctx-box J_MouseEneterLeave J_IconMoreNew")  
    for i in  comments:  
        temp=[]  
        Item=i.find_all("div",class_="row row-2 title")  #图书相关信息  
        temp.append(Item[0].text.strip())  
        shop=i.find_all("div",class_="row row-3 g-clearfix")  
        for j in shop:  
            a=j.find_all("span")  
            temp.append(a[-1].text)    #店铺名称  
        address=i.find_all('div',class_='location')   
        temp.append(address[0].text.strip())   #店铺所在地  
        priceandnum=i.find_all("div",class_="row row-1 g-clearfix")  
        for m in priceandnum:  
            Y=m.find_all('div',class_='price g_price g_price-highlight')  
            temp.append(Y[0].text.strip()) #商品价格  
            Num=m.find_all('div',class_='deal-cnt')  
            temp.append(Num[0].text.strip())   #购买人数  
        Infolist.append(temp)  
      
          
#   获取循环爬虫的页码数        
def getPageNum(firefox_login):  
    data=firefox_login.page_source  
    soup = BeautifulSoup(data,'lxml')   
    comments=soup.find_all("div", class_="total")  #匹配总的页数  
    pattern=re.compile(r'[0-9]')  
    pageNum=pattern.findall(comments[0].text)     # 将数字页数提取  
    pageNum=int(pageNum[0])  
    return pageNum     #用于循环的次数设置  
     
     
# 点击下一页 //更新数据。     
def NextPage(firefox_login):  
    firefox_login.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()  #点击下一页ajax刷新数据  
           
if __name__=='__main__':  
    firefox_login=init()    
    firefox_login=login(firefox_login)  
    Num=getPageNum(firefox_login)  
    for i in range(Num-1):  
        ObtainHtml(firefox_login)  
        NextPage(firefox_login)  
    print("信息爬取完成")  
