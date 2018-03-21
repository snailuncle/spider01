import requests
from lxml import etree
import json
import time
import sys
import re


def cnt(i, L=[]):
    if len(L)==0:
        L.append(0)
    L[0]+=i
    return L[0]

def get_one_page(url):
    try:
        html=requests.get(url).text
        html=re_search(html,"(?<=try{jQuery).*(?=\)}catch)")
        html=re_search(html.group(0),"{.*}")
        dict_obj=json.loads(html.group(0))
        comment_list=dict_obj['data']['feeds']
        for each in comment_list:
            comment={
                'name':each['name'],
                'description':each['description'],
                'releaseDate':timestamp_to_time(each['releaseDate'])
            }
            for key,value in comment.items():
                print(key+':'+value)
            print(str(cnt(1))+"条评论")
    except Exception as e:
        print(e)
        pass
#----------------------------------------------------------
def get_comment_number(url):
    html=requests.get(url).text
    html=re_search(html,"(?<=\"commentId\":).*?(?=,)")
    n1=html.group(0)
    print('评论总量为: '+n1)
    # 提取评论总量
    # 82000088848
    # 82727398548
    n2=n1[2:6]
    print(n2)
    n2=int(n2)
    return n2


def timestamp_to_time(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

# a = "2013-10-10 23:40:00"
def time_to_timestamp(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return str(timeStamp)+'000'

def time_to_str(t):
    str1=str(t)
    new_s=str1.replace('.','')
    s=new_s[0:13]
    return s

def re_search(str1,pattern):
    flags=re.S
    str2=re.search(pattern,str1,flags)
    return str2

def write_file(text):
    with open('temp_file.txt','w') as f:
        f.write(text)

def main():
    # 82000088848
    count=50
    count_str=str(count)
    #这个是最新的评论,用来提取评论总量
    url="http://api-t.iqiyi.com/feed/get_feeds?callback=jQuery&feedId=82571446448&agenttype=0&wallId=200091447"
    comment_number=get_comment_number(url)
    #这个链接是以前的评论  用feedId来控制评论数
    try:
        for i in range(comment_number,1000,-(count)):
            url="http://api-t.iqiyi.com/feed/get_feeds?callback=jQuery&agenttype=1&wallId=200091447&feedId=82"+str(i)+"88848&upOrDown=1&count="+count_str
            #每次提取20条
            print("提取评论的链接是: "+url)
            get_one_page(url)
            # time.sleep(1)
    except Exception as e:
        print(e)
        pass

if __name__=='__main__':
    main()
