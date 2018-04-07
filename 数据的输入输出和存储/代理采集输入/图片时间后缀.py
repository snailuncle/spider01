#coding:UTF-8
import time
#获取当前时间
time_now = int(time.time())
#转换成localtime
# time_local = time.localtime(time_now)
time_local = time.localtime(1523028263)
# 201523025468235                            
#转换成新的时间格式(2016-05-09 18:59:20)
dt = time.strftime(r"%Y/%m/%d{}%H:%M:%S".format(r'%%20'),time_local)
print(dt)
url='http://ip.zdaye.com/img/m_9f8a3bca7c108a2f.gif?{}'.format(dt)
print(url)
