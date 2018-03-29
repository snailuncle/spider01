
import json
import requests
from lxml import etree
import sys
import re
import time
import pymongo  
import random

# 建立mongo数据库
client=pymongo.MongoClient('localhost',27017)
#创建数据库
ceshi=client['ceshi'] 
#创建数据库中的表
url_list=ceshi['url_list3']
item_info=ceshi['item_info3']
#向表中添加一条记录
# url_list.insert_one({'url':'http://www.baidu.com'})

#获取个人二手商品列表
#第二页的网址   http://bj.58.com/diannao/0/pn2/
#第二页网址列表,   第一条信息url    http://zhuanzhuan.58.com/detail/978530122090135563z.shtml
def get_links_from(channel,pages,who_sells=0):
    #http://bj.58.com/diannao/0/pn2/
    list_view='{}{}/pn{}'.format(channel,str(who_sells),str(pages))
    print(list_view)
    web_data=requests.get(list_view).text
    # with open('58同城/个人二手列表页.txt','w',encoding='utf-8') as f:
    #     f.write(web_data)
    time.sleep(random.randint(5,30))
    web_data=etree.HTML(web_data)
    noinfo_xpath_str="//div[@class='mainleft']/div[contains(@class,'noinfo')]/div[@class='noinfotishi']/text()"
    if web_data.xpath(noinfo_xpath_str):
        print('第%d页,没有信息'%pages)
        pass
    else:
        xpath_str="//table[contains(@class,'tbimg')]/tbody/tr[contains(@class,'zzinfo')]/td[@class='t']/a[@onclick]/@href"
        links=web_data.xpath(xpath_str)
        for link in links:
            link=link.split('?')[0]
            url_list.insert_one({'url':link})
            get_item_info(link)
            print(link)



# channel='http://bj.58.com/diannao/'
# pages=200
# # who_sells=0
# get_links_from(channel,pages)





#目标  提取二手商品详情页的信息
def get_item_info(url):
    html=requests.get(url)
    html_text=html.text
    selector=etree.HTML(html_text)
    time.sleep(random.randint(5,10))
    




    #商品已下架的判断
    #/div[@class='info_lubotu clearfix']/div[@class='info_massege left']/div[@class='button_li']/span[@class='soldout_btn']
    soldout_xpath_str="//div[@class='info_lubotu clearfix']/div[@class='info_massege left']/div[@class='button_li']/span[@class='soldout_btn']"
    if selector.xpath(soldout_xpath_str):
        print('商品已下架,网址是: %s'%url)
        pass
    else:
        title_list=selector.xpath("//div[@class='info_lubotu clearfix']/div[@class='box_left_top']/h1[@class='info_titile']")
        title= title_list[0].text if title_list else '------'

        price_list=selector.xpath("//div[@class='info_lubotu clearfix']/div[@class='info_massege left']/div[@class='price_li']/span[@class='price_now']/i")
        price=price_list[0].text if price_list else '------'

        place_list=selector.xpath("//div[@class='info_lubotu clearfix']/div[@class='info_massege left']/div[@class='palce_li']/span/i")
        place=place_list[0].text if place_list else '------'

        baby_talk_list=selector.xpath("//div[@class='info_baby'][1]/div[@class='baby_talk']/div[@class='baby_kuang clearfix']/p")
        baby_talk=baby_talk_list[0].text if baby_talk_list else '------'
        
        item_info.insert_one({'title':title,'price':price,'place':place,'baby_talk':baby_talk})    
        print({'title':title,'price':price,'place':place,'baby_talk':baby_talk})



# url="http://zhuanzhuan.58.com/detail/78464423172z.shtml"
# get_item_info(url)
