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
import urllib
import json
# import os

class mailhelper(object):
    def __init__(self):
        self.mail_host="smtp.sina.cn" #设置服务器
        self.mail_user="username" #用户名
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

    def getContent(self,url):
        newhtml=requests.get(url,headers=self.headers,timeout=3).content
        new_selector=etree.HTML(newhtml)
        weibo_content_xpath_str="string(/html/body/div[starts-with(@id,'M_Ge')])"
        weibo_content=new_selector.xpath(weibo_content_xpath_str)
        pattern=r'赞\[\d*\]\s转发\[\d*\]\s评论\[\d*\].*|赞\[\d+\]\s原文转发\[\d+\]\s原文评论\[\d+\]'
        repl=''
        string=weibo_content
        content=re.sub(pattern, repl, string)






        return content

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
        'Cookie': 'SINAGLOBAL=1924335624445.1592.1521612311234; UM_distinctid=162e7df297143-028e7fea160d1a-37465265-15f900-162e7df297223; wvr=6; UOR=bbs.anjian.com,widget.weibo.com,www.baidu.com; SSOLoginState=1524883163; SCF=Al2_OzHAlbyaVCtImtWVFNtoJDRwl7IzQ-J25aGNCBDfYIpo9D7TKz8eF8TSlQ5hXIkM57-J_CvGPPBeBotEGdBQ.; SUHB=0qj1y-h-e7rD1C; _s_tentry=login.sina.com.cn; Apache=6033849433281.56.1524883166313; ULV=15248831663D62:19:14:4:6033D849433281.56.1524883166313:1524831821374; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWVs3TdKcmkTn28GCiwRkSf5JpX5oz75NHD95QEeheNS05NeKMNWs4Dqc_zi--Ri-i2i-iFi--ciKL2i-i8i--Ri-88i-z7i--fi-isiKnci--ciK.Ni-2fi--Ri-8si-82i--fiKy2iK.fi--Ri-8siKy2; ALF=1527475646; SUB=_2A25355DtDeRhGeRO6FUW8CnNzDuIHXVVKzClrDV8PUJbkNAKLVrakW1NUGxRMYQoegwnIxWAk_j_4_TzpY_BaQkp',
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
    weibo_id_list=['朱荣2800com','比特币大石','莱特币','比特币大石','荀森森','币圈渣渣辉','叫我韭菜哥就好了','14年买了个币','峰哥大话数字货币',]
#***********************这里写要发送到谁的邮箱******************************************************    
    mailto_list=['123@qq.com','23@qq.com']

    helper=xxoohelper()
    while True:
        try:
            now_time=time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
            # for index,app_id in enumerate(app_list):
            for _,nickname in enumerate(weibo_id_list):
                with open(nickname_file, 'r+') as f:
                    user_json_file=json.load(f)
                # 组装用户的主页地址url
                if nickname in user_json_file.keys():
                    user_id=user_json_file[nickname]
                else:
                    print('这个昵称没做过记录')
                    user_id=userid_find_from_nickname(nickname)                
                url='https://weibo.cn/u/%s'%user_id

                print(url)

                content=helper.getContent(url)
                # print(content)
                if helper.tocheck(content):
                    #如果微博作者是八大金刚,再发送邮件
        
                    if mailhelper().send_mail(mailto_list,"%s     微博"%nickname,content):
                        helper.tosave(content)
                        pass
                        # print(now_time+"发送成功")

                    else:
                        pass
                        # print(now_time+"发送失败")

                # 间隔十秒
                time.sleep(10)
                # raise RuntimeError('testError')
        except Exception as e:
            print(e)
            pass

















