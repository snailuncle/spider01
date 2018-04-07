import requests
import re,os,time,json,sys
import subprocess as sp

url='http://ip.zdaye.com/img/m_9f8a3bca7c108a2f.gif?2018/4/6%2019:12:58'
def timestamp_extract(url):
    url='http://ip.zdaye.com/img/m_82cc4b8fc1f7f5ad.gif?2018/4/6%2021:24:42'
    pattern=r'(?<=\?).*'
    dt=re.search(pattern,url).group()
    dt=re.sub(r'[/%]',' ',dt)
    dt=dt[0:-10]+dt[-8:]
    # print(dt)
    # sys.exit()
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y %m %d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)

    return int(timestamp)
timestamp=timestamp_extract(url)
#运行本脚本至少等待5分钟
#视网络情况和电脑等级而定.
#不加UA不返回正确信息
old_headers='''abc%s
hhh'''%timestamp

print(old_headers)
