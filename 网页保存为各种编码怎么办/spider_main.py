#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 01:11:03 2018

@author: moqiu
"""

import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                print('ok1')
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                print('ok2')
                self.urls.add_new_urls(new_urls)
                print('ok3')
                self.outputer.collect_data(new_data)
                print('ok4')
                
                
                if count == 200:
                    break
                count = count+1
            except:
                print('craw failed')
                
        self.outputer.output_html()
        print('ok5')
            
        
        
   
     
        
    

if __name__ =="__main__":
    root_url = "https://baike.baidu.com/item/%E6%A0%BC%E5%8A%9B%E9%9B%86%E5%9B%A2/4164499?fr=aladdin&fromid=1446821&fromtitle=%E6%A0%BC%E5%8A%9B"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)#用craw操作来启动
#
    

