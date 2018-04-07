import json
proxies={'http':'17.66.199.61:49446'}
proxies=json.dumps(proxies)
proxies=json.loads(proxies)
print(proxies)
print(type(proxies))
