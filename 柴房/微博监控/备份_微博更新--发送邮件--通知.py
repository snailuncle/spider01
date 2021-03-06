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
        self.mail_user="username" #用户名
        self.mail_pass="password" #口令
        self.mail_postfix="sina.cn" #发件箱的后缀

    def send_mail(self,to_list,sub,content):
        me="xxoohelper"+"<"+self.mail_user+'@'+self.mail_postfix+">"
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
        except Exception as e:
            print(e)
            return False

class xxoohelper(object):
    def __init__(self):
        self.url="https://weibo.cn/"
        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_T_WM=ca882e917b7e2f07ef05c0ed599d19ea; SSOLoginState=1524831987; ALF=1527423987; SCF=Al2_OzHAlbyaVCtImDtWVFNtoJRwl7IzQ-J25aGNCBDfYKw_nks7Hm6BzzMT-YnVtgxHDac8C75k61BiebVkQka0.; SUB=_2A25352ajDeRhGeRO6FUDW8CnNzDuIHXVVKArrrDV6PUNbktAKLRf9kW1NUGxRMVY3hBQ4cZ2y0H0R67hHgCkX9Fp6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5KzhUgL.Foz7e0MNehMpS0M2dJLoIXnLxKnLB.BLB.zDLxKqL1-BLB.-LxKnLB--LBo5LxK-LB.qL1hqLxKqL1KMLBK-LxKnLB-qLB-BLxK-L12BL1K-LxKnLB-qL12Bt; SUHB=0ebsorE5BJOA4e',
            'Host': 'weibo.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        }

    def getContent(self):
        newhtml=requests.get(self.url,headers=self.headers,timeout=3).content
        new_selector=etree.HTML(newhtml)
        content=new_selector.xpath("//span[@class='ctt']")
        newcontent=content[0].xpath('string(.)').replace('http://','')
        sendtime=new_selector.xpath("//span[@class='ct']/text()")[0]
        name=new_selector.xpath("//div[@class='c']/div/a[@class='nk']/text()")[0]
        sendtext=name+newcontent+sendtime
        return sendtext,name

    def tosave(self,text):
        f=open('weibo.txt','w',encoding='utf-8')
        f.write(text+'\n')
        f.close()

    def tocheck(self,data):
        if not os.path.exists('weibo.txt'):
            return True
        else:
            f=open('weibo.txt','r',encoding='utf-8')
            existweibo=f.read()
            # print('文本文件中的数据是: '+existweibo)
            try:
                new_data=self.re_search(data,'.+(?=(分钟|小时)前)').group(0)
                new_data=new_data[:-2]
            except Exception:
                new_data=data


            # print('接收到的数据是: '+data)
            if new_data in existweibo:
                return False
            else:
                return True

    def re_search(self,str1,pattern):
        flags=re.S
        str2=re.search(pattern,str1,flags)
        return str2


if __name__=='__main__':
    mailto_list=['104@qq.com']
    helper=xxoohelper()
    while True:
        now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        content,name=helper.getContent()
        if helper.tocheck(content):
            if mailhelper().send_mail(mailto_list,name+now_time+"  给女神发送邮件成功啦",content):
                print(now_time+"发送成功")
                helper.tosave(content)
            else:
                print(now_time+"发送失败")
        else:
            print(now_time+"  这条微博发过邮件了")

        time.sleep(6)


















