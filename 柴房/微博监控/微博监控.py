#!/usr/bin/python
#由于阿里云服务器SMTP端口25不能使用
#改为SSL  465端口
import smtplib
from email.mime.text import MIMEText
import requests
from lxml import etree
import os
import time
import sys
import re

class mailhelper(object):
    def __init__(self):
        self.mail_host="smtp.sina.cn" #设置服务器
        self.mail_user="user" #用户名
        self.mail_pass="password" #口令
        self.mail_postfix="sina.cn" #发件箱的后缀

    def send_mail(self,to_list,sub,content):
        me="weibo"+"<"+self.mail_user+'@'+self.mail_postfix+">"
        msg=MIMEText(content,_subtype='plain',_charset='utf-8')
        msg["Subject"]=sub
        msg["From"]=me
        msg['To']=";".join(to_list)
        try:
            server=smtplib.SMTP_SSL()
            server.connect(self.mail_host,465)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me,to_list,msg.as_string())
            server.close()
            return True
        except Exception:
            return False

class xxoohelper(object):
    def __init__(self):
        self.weibo_path='weibo_content_record.txt'
        self.url="https://weibo.cn/"
        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_T_WM=ca882e917b7e2f07ef05c0ed599d19ea; SSOLoginState=1524831987; ALF=1527423987; SCF=Al2_OzHAlbyaVCtImtWVFNtoJRwl7IzQ-J25aGNCBDfYKw_nks7Hm6BzzMT-YnVtgxHDac8C75k61BiebVkQka0.; SUB=_2A25352ajDeRhGeRO6FUW8CnNzDuIHXVVKArrrDV6PUNbktAKLRf9kW1NUGxRMVY3hBQ4cZ2y0H0R67hHgCkX9Fp6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5KzhUgL.Foz7e0MNehMpS0M2dJLoIXnLxKnLB.BLB.zLxKqL1-BLB.-LxKnLB--LBo5LxK-LB.qL1hqLxKqL1KMLBK-LxKnLB-qLB-BLxK-L12BL1K-LxKnLB-qL12Bt; SUHB=0ebsorE5BJOA4e',
            'Host': 'weibo.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        }

    def getContent(self):
        newhtml=requests.get(self.url,headers=self.headers,timeout=3).content
        new_selector=etree.HTML(newhtml)

        # 提取微博的作者,内容,发布时间
        weibo_authors=new_selector.xpath("/html/body/div[@id]/div/a[@class='nk']")
        weibo_contents=new_selector.xpath("/html/body/div[@id]/div/span[@class='ctt']")
        weibo_pubtimes=new_selector.xpath("/html/body/div[@id]/div/span[@class='ct']")
        weibo_content_dict_list=[]
        for i in range(6):
            weibo_author=weibo_authors[i].xpath('string(.)') if weibo_authors[i].xpath('string(.)') else ''
            weibo_content=weibo_contents[i].xpath('string(.)') if weibo_contents[i].xpath('string(.)') else ''
            weibo_pubtime=weibo_pubtimes[i].xpath('string(.)') if weibo_pubtimes[i].xpath('string(.)') else ''

            dict={
                'weibo_author':weibo_author,
                'weibo_content':weibo_content,
                'weibo_pubtime':weibo_pubtime
            }
            weibo_content_dict_list.append(dict)
        # print(dict)
        # {'weibo_author': '朱荣2800com', 'weibo_content': '愿你们余生只笑不哭，白头偕老。[心][心] 全球笑点搜罗的秒拍视频 \u200b\u200b\u200b', 'weibo_pubtime': '今天 21:32\xa0来自微博 weibo.com'}

        return weibo_content_dict_list

    def tosave(self,data):
        data=data['weibo_content']        
        f=open(self.weibo_path,'a+',encoding='utf-8')
        f.write(data)
        f.close()

    #检查是否保存过该条微博,没有保存过的话,返回True,然后发送邮件
    def tocheck(self,data):
        data=data['weibo_content']
        if not os.path.exists(self.weibo_path):
            return True
        else:
            with open(self.weibo_path,'r',encoding='utf-8') as f:
                existweibo=f.read()
            # print('接收到的数据是: '+data)
            if data in existweibo:
                return False
            else:
                return True


if __name__=='__main__':
    weibo_id_list=['朱荣2800com','比特币大石','莱特币','比特币大石','荀森森','币圈渣渣辉','叫我韭菜哥就好了','14年买了个币','峰哥大话数字货币',]
    # mailto_list=['123@qq.com','23@qq.com']
    mailto_list=['1789@qq.com']
    try:
        helper=xxoohelper()
        while True:
            now_time=time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
            content_dict_list=helper.getContent()
            print(content_dict_list)
            for i in range(6):
                content_dict=content_dict_list[i]
                # print(content_dict)
                if helper.tocheck(content_dict):
                    #如果微博作者是八大金刚,再发送邮件
                    if content_dict['weibo_author'] in weibo_id_list:
                        now_time=content_dict['weibo_pubtime']
                        if mailhelper().send_mail(mailto_list,content_dict['weibo_author']+now_time+"  关注的人微博有更新",content_dict['weibo_content']):
                            helper.tosave(content_dict)
                            pass
                            # print(now_time+"发送成功")

                        else:
                            pass
                            # print(now_time+"发送失败")
                else:
                    pass
                    # print(now_time+"  这条微博发过邮件了")

            time.sleep(10)
    except Exception:
        pass

















