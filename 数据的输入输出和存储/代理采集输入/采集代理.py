#coding:UTF-8
import time,re,sys

def timestamp_extract(url):
    url='http://ip.zdaye.com/img/m_4f63daa4571c0b63.gif?2018/4/6%2019:12:58'
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

    return int(timestamp)-20
timestamp=timestamp_extract('')
print(timestamp)


