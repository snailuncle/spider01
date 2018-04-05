#代理
from 代理 import proxy_get
import json
one_proxy=proxy_get()
print("代理: = "+json.dumps(one_proxy))
#UA
from fake_useragent import UserAgent
ua=UserAgent()
first_ua=ua.random
print("UA: = "+first_ua)

