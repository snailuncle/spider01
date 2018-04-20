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
import configparser


class SinaSpider(object):
    def __init__(self):
        self.current_url='新浪微博/current_url.txt'
        self.config_path='新浪微博/keyword.ini'
        # self.current_keyword='keyword.ini'
        # self.current_keyword='新浪微博/keyword.ini'
        self.keyword_list=["杨幂"]
        self.host_url="https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D"
        b = os.path.exists(self.current_url)  
        if b:  
            print(self.current_url)  
        else:  
            with open(self.current_url,'w') as f:
                f.write('')  
        b = os.path.exists(self.config_path)  
        if b:  
            print(self.config_path)  
        else:  
            with open(self.config_path,'w') as f:
                f.write('')    
        # conf = configparser.ConfigParser()  
        self.section_name="section_one"

        cfg = configparser.ConfigParser() 
        cfg.read(self.config_path)
        secs=cfg.sections()
        if self.section_name in secs:
            print(self.section_name+"已存在于配置文件")
            pass
        else:
            print(self.section_name+"不存在于配置文件")
            cfg.add_section(self.section_name)
            for i in range(len(self.keyword_list)):
                cfg.set(self.section_name,self.keyword_list[i],'2')

            f = open(self.config_path,'w')
            cfg.write(f)
            f.close()                    
     


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
            print(url)
            if not self.check_url(url):
                print("第%d页爬过了: "%1+url)  
            else:        
                html=requests.get(url,timeout=3).content
                # ************************************************************************************************************************************************
                print(html)
                self.save_current_url(url)
                html_dict=json.loads(html)
                # new_selector=etree.HTML(html)

                # cards  1     card_group      0       mblog  西梅皇马的信息
                # cards  1     card_group      1       mblog  高晓松  的信息

                # cards  2     card_group      0       mblog  韦恩斯破产的信息

                # cards  4     card_group      0-7       mblog  预算2亿的信息


                gaoxiaosong_dict_cards_1=html_dict['data']['cards'][1]['card_group'][0]
                blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_1)
                self.save_file(keyword,str(blog_dict))
                print(str(blog_dict))

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



# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B1%82%E8%B4%AD&page=2
# https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D求购&page=2

# data     cards      0       card_group      0-9     都有      
#                                              0      mblog   
    def getContent_next_url(self,keyword):
        # &page=2

        # with open(self.config_path,'r+') as f:
        #     cfg = configparser.ConfigParser() 
        #     cfg.readfp(f)
        #     secs=cfg.sections()
        #     page_number=int(cfg.get(self.section_name, keyword))
        #     # cfg.set('section',self.keyword_list[i],'0')
        #     # cfg.write(f)
        
        cfg = configparser.ConfigParser() 
        cfg.read(self.config_path)
        page_number=int(cfg.get(self.section_name, keyword))
        cfg.set(self.section_name,keyword,str(page_number))
        # print(cfg)
        # sys.exit()
        f = open(self.config_path,'w')
        cfg.write(f)
        f.close()         


        content_isnot_empty=True
        for i in range(page_number,1000):
            try:
                time.sleep(TIME_INTERVAL)
                if content_isnot_empty is False:
                    print("break for 1000***********************")
                    break
                url=self.host_url+keyword
                if not self.check_url(url+"&page="+str(i)):
                    print("第%d页爬过了: "%i+url+"&page="+str(i))
                    continue
                print("现在爬第%d页************"%i)
                html=requests.get(url+"&page="+str(i),timeout=3).content

                cfg = configparser.ConfigParser() 
                cfg.read(self.config_path)
                cfg.set(self.section_name,keyword,str(i+1))
                f = open(self.config_path,'w')
                cfg.write(f)
                f.close()     




                # html=requests.get("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D感觉棒棒哒&page=68",timeout=3).content
                if len(html)<100:
                    print('第%d页没有内容,跳出1000页的循环******************: '%i+url+"&page="+str(i))
                    break
                self.save_current_url(url+"&page="+str(i))
                html_dict=json.loads(html)
                gaoxiaosong_dict_cards_1=html_dict['data']['cards'][0]['card_group']
                for j in range(10):
                    try:
                        blog_dict=False
                        gaoxiaosong_dict_cards_2=gaoxiaosong_dict_cards_1[j]
                        blog_dict=self.get_blog_dict(gaoxiaosong_dict_cards_2)
                        if not blog_dict:
                            content_isnot_empty=False
                            break
                        self.save_file(keyword,str(blog_dict))
                        print(blog_dict)
                    except Exception as e:
                        pass
                print('current_url: '+str(i)+"   "+url+"&page="+str(i))
                self.save_current_url(url+"&page="+str(i))
            except Exception as e:
                print(e)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                pass



    def save_current_url(self,url):
        f=open(self.current_url,'a',encoding='utf-8')
        f.write(url)
        f.write("\n\n")
        f.close()
   

    def save_file(self,path_name,text):
        f=open(path_name+'.txt','a',encoding='utf-8')
        f.write(text+"\n\n")
        f.close()

    def re_search(self,str1,pattern):
        flags=re.S
        str2=re.search(pattern,str1,flags)
        return str2

    def check_url(self,url):
        with open(self.current_url, 'r',encoding='utf-8') as f:   
            for line in f.readlines():                          
                line = line.strip()                   
                if not len(line):       
                    continue    
                else:
                    #比较当前url和已经爬过的url是否重复
                    if url==line:
                        return False
                        break
            else:
                return True
        



if __name__=='__main__':
    TIME_INTERVAL=1
    spider=SinaSpider()
    for keyword in spider.keyword_list:
        spider.getContent(keyword)
        spider.getContent_next_url(keyword)












