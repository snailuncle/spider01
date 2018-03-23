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
MAIL_USER_NAME="cmyyq"
MAIL_PASSWORD="123"
mailto_list=['123456789@qq.com']
now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
sub_title="美团徐州店铺信息"
content="美团徐州店铺信息"
class mailhelper(object):
    def __init__(self):
        self.mail_host="smtp.sina.cn" #设置服务器
        self.mail_user=MAIL_USER_NAME #用户名
        self.mail_pass=MAIL_PASSWORD #口令
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

if mailhelper().send_mail(mailto_list,now_time+sub_title,content):
    print(now_time+"发送成功")
else:
    print(now_time+"发送失败")



















