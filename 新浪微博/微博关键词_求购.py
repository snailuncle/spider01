# cards  1     card_group      0       mblog  西梅皇马的信息
# cards  1     card_group      1       mblog  高晓松  的信息

# cards  2     card_group      0       mblog  韦恩斯破产的信息

# cards  4     card_group      0-7       mblog  预算2亿的信息


# 求购  求买  想买  求推荐
#https://m.weibo.cn/p/searchall?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD

import requests
from lxml import etree
import os
import time
import sys
import re
import json


class SinaSpider(object):
    def __init__(self):
        # self.url="https://m.weibo.cn/p/searchall?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD"
        self.keyword="求购"
        #         https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D求购&page=2
        # self.url="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD"
        self.url="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D"+self.keyword
        # self.headers={
        #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate, br',
        #     'Accept-Language':'zh-CN,zh;q=0.9',
        #     'Cache-Control':'max-age=0',
        #     'Connection':'keep-alive',
        #     'Cookie':'_T_WM=040e9cc680ab0ab1c1e07e8bac4b1318; SCF=ApEUyfHcHBch9XwUjgacYsLdDzisBMd4uYaQfy65RsYUByK-N4ovJxIlRDdHwaOHRr3tZBZNv-LVdGgndPrAd09HM.; SUHB=05i7QX7RM69ooG; SUB=_2AkMt6tICdcPd3xrAFRm_8SzGzja4pH-jyeP7v0An7oJhMyPRh77g9VqSdutBF-XLjuCpZTM03O0SjSZ8gZu3XOzCKW; WEIBOCN_FROM=1110006a030; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3Dsearchall%26fid%3D100103%25E6%25B1%2582%25E8%25B4%25AD%26uicode%3D10000011',
        #     'Host':'m.weibo.cn',
        #     'Upgrade-Insecure-Requests':'1',
        #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36',
        # }

    def get_blog_dict(self,gaoxiaosong_dict_cards):
        blog_author=gaoxiaosong_dict_cards['mblog']['user']['screen_name']
        blog_write_time=gaoxiaosong_dict_cards['mblog']['created_at']
        blog_content=gaoxiaosong_dict_cards['mblog']['text']
        blog_content = etree.HTML(blog_content)
        blog_content = blog_content.xpath("*")[0].xpath('string(.)').strip()
        blog_dict={
            'author':blog_author,
            'time':blog_write_time,
            'content':blog_content
        }
        return blog_dict

    def getContent(self):
        try:
            # html=requests.get(self.url,headers=self.headers,timeout=3).text
            html=requests.get(self.url,timeout=3).content
            html_dict=json.loads(html)
            # new_selector=etree.HTML(html)

            # cards  1     card_group      0       mblog  西梅皇马的信息
            # cards  1     card_group      1       mblog  高晓松  的信息

            # cards  2     card_group      0       mblog  韦恩斯破产的信息

            # cards  4     card_group      0-7       mblog  预算2亿的信息


            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][1]['card_group'][0]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(str(blog_dict))
            print(blog_dict)

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][1]['card_group'][1]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(str(blog_dict))
            print(blog_dict)        

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][2]['card_group'][0]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(str(blog_dict))
            print(blog_dict)

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][4]['card_group']
            for i in range(8):
                gaoxiaosong_dict_cards_2=gaoxiaosong_dict_cards_1[i]
                blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_2)
                self.save_file(str(blog_dict))
                print(blog_dict)
        except Exception as e:
            pass

        # sys.exit()

# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD&page=2
# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D求购&page=2

# data     cards      0       card_group      0-9     都有      
#                                              0      mblog   
    def getContent_next_url(self):
        # &page=2
        for i in range(2,1000):
            try:
                time.sleep(6)
                html=requests.get(self.url+"&page="+str(i),timeout=3).content
                html_dict=json.loads(html)
                gaoxiaosong_dict_cards_1=html_dict['data']['cards'][0]['card_group']
                for i in range(10):
                    try:
                        gaoxiaosong_dict_cards_2=gaoxiaosong_dict_cards_1[i]
                        blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_2)
                        self.save_file(str(blog_dict))
                        print(blog_dict)
                    except Exception as e:
                        pass
            except Exception as e:
                pass


    def save_file(self,text):
        f=open('qiugou.txt','a',encoding='utf-8')
        f.write(text)
        f.close()

    def re_search(self,str1,pattern):
        flags=re.S
        str2=re.search(pattern,str1,flags)
        return str2





if __name__=='__main__':
    spider=SinaSpider()
    spider.getContent()
    spider.getContent_next_url()












