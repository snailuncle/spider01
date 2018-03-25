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
        self.keyword_list=["这次买到","买给妈妈","买之前","好用","感觉棒棒哒","入手","相见恨晚","下决心买","可以买","特想要","好不好"]
        #         https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D求购&page=2
        # self.url="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD"
        self.host_url="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D"
        # self.url_list=[]
        # for i in range(len(self.keyword)):
        #     self.url_list=self.url_list.append(self.host_url+self.keyword[i])
        #     self.url_list="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D"+self.keyword
        # self.headers={
        #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate, br',
        #     'Accept-Language':'zh-CN,zh;q=0.9',
        #     'Cache-Control':'max-age=0',
        #     'Connection':'keep-alive',
        #     'Cookie':'_T_WM=040e9cc680ab0b1318; SCF=ApEUyfHcHBch9XwUjgacYsLdDzisBN4ovJxIlRDdHwaOHRr3tZBZNv-LVdGgndPrAd09HM.; SUHB=05i7QX7RM69ooG; SUB=_2AkMt6tICdcPdtBF-XLjuCpZ3XOzCKW; WEIBOCN_FROM=1110006a030; M_WEIBOCN_PARAMS=featureco0000011%26lfid%3Dsearchall%26fid%3D1582%25E8%25B4%25AD%26uicode%3D10000011',
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

    def getContent(self,keyword):
        try:
            # html=requests.get(self.url,headers=self.headers,timeout=3).text
            url=self.host_url+keyword
            html=requests.get(url,timeout=3).content
            html_dict=json.loads(html)
            # new_selector=etree.HTML(html)

            # cards  1     card_group      0       mblog  西梅皇马的信息
            # cards  1     card_group      1       mblog  高晓松  的信息

            # cards  2     card_group      0       mblog  韦恩斯破产的信息

            # cards  4     card_group      0-7       mblog  预算2亿的信息


            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][1]['card_group'][0]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(keyword,str(blog_dict))
            print(blog_dict)

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][1]['card_group'][1]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(keyword,str(blog_dict))
            print(blog_dict)        

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][2]['card_group'][0]
            blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
            self.save_file(keyword,str(blog_dict))
            print(blog_dict)

            gaoxiaosong_dict_cards_1=html_dict['data']['cards'][4]['card_group']
            for i in range(8):
                gaoxiaosong_dict_cards_2=gaoxiaosong_dict_cards_1[i]
                blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_2)
                self.save_file(keyword,str(blog_dict))
                print(blog_dict)
        except Exception as e:
            pass

        # sys.exit()

# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD&page=2
# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D求购&page=2

# data     cards      0       card_group      0-9     都有      
#                                              0      mblog   
    def getContent_next_url(self,keyword):
        # &page=2
        content_isnot_empty=True
        for i in range(2,1000):
            try:
                time.sleep(6)
                if content_isnot_empty is False:
                    break
                url=self.host_url+keyword
                html=requests.get(url+"&page="+str(i),timeout=3).content
                html_dict=json.loads(html)
                gaoxiaosong_dict_cards_1=html_dict['data']['cards'][0]['card_group']
                for i in range(10):
                    try:
                        gaoxiaosong_dict_cards_2=gaoxiaosong_dict_cards_1[i]
                        blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_2)
                        if not blog_dict:
                            content_isnot_empty=False
                            break
                        self.save_file(keyword,str(blog_dict))
                        print(blog_dict)
                    except Exception as e:
                        pass
            except Exception as e:
                pass


    def save_file(self,path_name,text):
        f=open(path_name+'.txt','a',encoding='utf-8')
        f.write(text)
        f.close()

    def re_search(self,str1,pattern):
        flags=re.S
        str2=re.search(pattern,str1,flags)
        return str2

    def check_file_size(self,keyword):
        file_name=keyword+'.txt'
        s=os.path.getsize(file_name)
        return s
        



if __name__=='__main__':
    spider=SinaSpider()
    for keyword in spider.keyword_list:
        spider.getContent(keyword)
        spider.getContent_next_url(keyword)












