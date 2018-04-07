#代理
from 代理 import proxy_get
import json
one_proxy=proxy_get()
print(one_proxy)
print("代理: = "+json.dumps(one_proxy))
#UA
from fake_useragent import UserAgent
ua=UserAgent()
rnd_ua=ua.random
print("UA: = "+rnd_ua)

#目标:下载爱奇艺vip电影
#捉妖记2

#爱奇艺捉妖记电影链接
#http://www.iqiyi.com/v_19rr7pge9c.html#vfrm=2-4-0-1
