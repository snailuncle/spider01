

import requests
import time,os,re,json
proxies=         {'http': 'http://27.204.42.166:28719'}
url='http://httpbin.org/ip'
r=requests.get(url,timeout=15,proxies=proxies)

print('*'*50)
print(r.text)

with open(r'D:\spider01\数据的输入输出和存储\proxies.txt','a') as f:
    f.write(str(proxies)+'\n\n')
