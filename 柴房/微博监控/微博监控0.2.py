#!/usr/bin/python
#由于阿里云服务器SMTP端口25不能使用
#改为SSL  465端口
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import requests
from lxml import etree
import os
import time
import sys
import re
import urllib
import json
import traceback
# import os

class mailhelper(object):
    def __init__(self):
        # self.mail_host="smtp.sina.cn" #设置服务器
        # self.mail_user="cmyyq" #用户名
        # self.mail_pass="lambda123" #口令
        # self.mail_postfix="sina.cn" #发件箱的后缀

        
        self.mail_host="smtp.qq.com" #设置服务器
        self.mail_user="342452" #用户名
        self.mail_pass="hmqctechjc" #口令
        self.mail_postfix="qq.com" #发件箱的后缀



        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_T_WM=ca882e917b7e2f07ef05c0ed599d19ea; SSOLoginState=1524831987; ALF=1527423987; SCF=Al2_OzHAlbyaVCtImtWVFNtoJRwl7IzQ-J25aGNDCBDfYKw_nks7Hm6BzzMT-YnVtgxHDac8C75k61BiebVkQka0.; SUB=_2A25352ajDeRhGeRO6FUW8CnNzDuIHXVVKArrrDV6PUNbktAKLRf9kW1NUGxRMVY3hBQ4cZ2y0H0R67hHgCkX9Fp6; SUBP=0033WrSXqPxfM725Ws9jqgMF5DD5529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5KzhUgL.Foz7e0MNehMpS0M2dJLoIXnLxKnLB.BLB.zLxKqL1-BLB.-LxKnLB--LBo5LxK-LB.qL1hqLxKqL1KMLBK-LxKnLB-qLDB-BLxK-L12BL1K-LxKnLB-qL12Bt; SUHB=0ebsorE5BJOA4e',
            'Host': 'weibo.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        }
    #发送单纯的文字内容
    # def send_mail(self,to_list,sub,content):
    #     me="weibo"+"<"+self.mail_user+'@'+self.mail_postfix+">"
    #     msg=MIMEText(content,_subtype='plain',_charset='utf-8')
    #     msg["Subject"]=sub
    #     msg["From"]=me
    #     msg['To']=";".join(to_list)
    #     try:
    #         server=smtplib.SMTP_SSL()
    #         server.connect(self.mail_host,465)
    #         server.login(self.mail_user,self.mail_pass)
    #         server.sendmail(me,to_list,msg.as_string())
    #         server.close()
    #         return True
    #     except Exception:
    #         return False

    #发送带图片的邮件
    def send_mail(self,to_list,sub,user_homepage,content,img=None):
        # me="weibo"+"<"+self.mail_user+'@'+self.mail_postfix+">"
        me="<"+self.mail_user+'@'+self.mail_postfix+">"
        msg=MIMEMultipart('alternative') 
        if img:
            newhtml=requests.get(img,headers=self.headers,timeout=3).text
            part1 = MIMEText(user_homepage,'html','utf-8') 
            part2 = MIMEText('<div><br><b>%s</b></div><br>'%content,'html','utf-8') 
            part3 = MIMEText(newhtml,'html','utf-8') 
            text="<div><br><b>若图片看不见, 请点击上方的  显示图片</b></div><br>"
            part_up = MIMEText(text,'html','utf-8') 
            msg.attach(part_up) 
            msg.attach(part1) 
            msg.attach(part2) 
            msg.attach(part3) 
        else:
            msgText = MIMEText('<b>%s</b><br>'%content,'html','utf-8') 
            msg.attach(msgText)          

        msg["Subject"]=sub
        msg["From"]=me
        msg['To']=";".join(to_list)
        try:
            server=smtplib.SMTP_SSL()
            server.connect(self.mail_host,465)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me,to_list,msg.as_string())
            server.close()
            # print('方法内打印: 发送成功')
            return True
        except Exception:
            # print('*'*66)
            # print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
            # print('*'*66)
            return False
   









class xxoohelper(object):
    def __init__(self):
        self.weibo_path='weibo_content_record.txt'
        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_T_WM=ca882e917b7e2f07ef05c0ed599d19ea; SSOLoginState=1524831987; ALF=1527423987; SCF=Al2_OzHAWs9jqgMF5DD5529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5KzhUgL.Foz7e0MNehMpS0M2dJLoIXnLxKnLB.BLB.zLxKqL1-BLB.-LxKnLB--LBo5LxK-LB.qL1hqLxKqL1KMLBK-LxKnLB-qLDB-BLxK-L12BL1K-LxKnLB-qL12Bt; SUHB=0ebsorE5BJOA4e',
            'Host': 'weibo.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        }

#************************此处提取微博内容**************************************************
    def getContent(self,url):
        newhtml=requests.get(url,headers=self.headers,timeout=3).content
        new_selector=etree.HTML(newhtml)
        weibo_content_xpath_str="string(/html/body/div[starts-with(@id,'M_Ge')])"
        weibo_content=new_selector.xpath(weibo_content_xpath_str)
        pattern=r'赞\[\d*\]\s转发\[\d*\]\s评论\[\d*\].*|赞\[\d+\]\s原文转发\[\d+\]\s原文评论\[\d+\]'
        repl=''
        string=weibo_content
        content=re.sub(pattern, repl, string)

        if '[图片]' in content:
            # //a[text()=‘下一页’]/@href就是
            weibo_img_xpath_str="/html/body/div[starts-with(@id,'M_Ge')]/div/a[text()='图片']/@href"
            weibo_content_img_url=new_selector.xpath(weibo_img_xpath_str)[0]
            # print('eturn [content,weibo_content_img_url]')
            # print(weibo_content_img_url)
            return [content,weibo_content_img_url]

        # print(content)
        # sys.exit()
        return [content]




    def tosave(self,data):
        f=open(self.weibo_path,'a+',encoding='utf-8')
        f.write(data)
        f.close()

    #检查是否保存过该条微博,没有保存过的话,返回True,然后发送邮件
    def tocheck(self,data):
        if not os.path.exists(self.weibo_path):
            return True
        else:
            with open(self.weibo_path,'r',encoding='utf-8') as f:
                existweibo=f.read()
            if data in existweibo:
                return False
            else:
                return True


def userid_find_from_nickname(weibo_nickname):
    weibo_nickname_urllib_parse_quote=urllib.parse.quote(weibo_nickname)
    url="http://open.weibo.com/widget/ajax_getuidnick.php?rnd=0.402559111556819"
    headers={
        'Referer': 'http://open.weibo.com/widget/followbutton.php',
        'Origin': 'http://open.weibo.com',
        'Content-Length': '3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '19:14:4:6033D849433281.56.1524883166313:1524831821374; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5oz75NHD95QEeheNS05NeKMNWs4Dqc_zi--Ri-i2i-iFi--ciKL2i-i8i--Ri-88i-z7i--fi-isiKnci--ciK.Ni-2fi--Ri-8si-82i--fiKy2iK.fi--Ri-8siKy2; ALF=1527475646; SUB=_2A25355DtDeRhGeRO6FUW8CnNzDuIHXVVKzClrDV8PUJbkNAKLVrakW1NUGxRMYQoegwnIxWAk_j_4_TzpY_BaQkp',
        'Host': 'open.weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
    }

    d={'nickname':weibo_nickname_urllib_parse_quote} 

    newhtml=requests.post(url,headers=headers,data=d,timeout=3).text
    newhtml=json.loads(newhtml)
    #查询到用户ID之后保存到文件,避免频繁查找.
    weibo_userid=newhtml['data']
    nickname_file='nickname.txt'
    weibo_userid_json={}

    if  os.path.exists(nickname_file):
        if os.path.getsize(nickname_file)<6:
            pass
        else:
            with open(nickname_file, 'r+') as f:
                weibo_userid_json=json.load(f)
    #添加用户信息
    weibo_userid_json[weibo_nickname]=weibo_userid
    with open(nickname_file,'r+') as f:
        json.dump(weibo_userid_json,f)

    return weibo_userid
    





if __name__=='__main__':
    #初始化nickname.txt
    nickname_file='nickname.txt'
    if  os.path.exists(nickname_file):
        pass 
    else:
        content={}
        with open(nickname_file,"w") as f:
            f.write(json.dumps(content))
#***********************这里写微博昵称******************************************************            
    weibo_id_list=['朱荣2800com','比特币大石','莱特币','荀森森','币圈渣渣辉','叫我韭菜哥就好了','14年买了个币','峰哥大话数字货币',]
#***********************这里写要发送到谁的邮箱******************************************************    
    mailto_list=['1789500304@qq.com','864544425@qq.com']
    # mailto_list=['1789500304@qq.com','864544425@qq.com']

    helper=xxoohelper()
    while True:
        try:
            now_time=time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
            # for index,app_id in enumerate(app_list):
            # print(weibo_id_list)
            for _,nickname in enumerate(weibo_id_list):
                # print(nickname)
                with open(nickname_file, 'r+') as f:
                    user_json_file=json.load(f)
                # 组装用户的主页地址url
                if nickname in user_json_file.keys():
                    user_id=user_json_file[nickname]
                else:
                    # print('这个昵称没做过记录')
                    user_id=userid_find_from_nickname(nickname)                
                url='https://weibo.cn/u/%s'%user_id

                print(url)

                content=helper.getContent(url)
                # print(content)
                if len(content)==2:
                    img_url=content[1]
                    # print('imgurl=%s'%img_url)
                    content=content[0]
                else:
                    img_url=None
                    content=content[0]                    
                # print(content)
                if helper.tocheck(content):
                    comcom='https://weibo.com/u/%s'%user_id
                    user_homepage="<p><a href=%s >%s</a></p><br><br> "%(comcom,nickname)
                    if mailhelper().send_mail(mailto_list,"%s     微博"%nickname,user_homepage,content,img_url):
                        helper.tosave(content)
                        # print(now_time+"发送成功")
                        pass

                    else:
                        # print(now_time+"发送失败")
                        pass

                # 间隔十秒
                time.sleep(30)
                # raise RuntimeError('testError')
        except Exception:
            # print('*'*66)
            # print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
            # print('*'*66)
            pass




