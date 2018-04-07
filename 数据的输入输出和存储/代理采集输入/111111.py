# #使用session保持连接
# # 创建一个session对象 
# s = requests.Session() 
# # 设置session对象的auth属性，用来作为请求的默认参数 
# s.auth = ('user', 'pass') 
# # 设置session的headers属性，通过update方法，将其余请求方法中的headers属性合并起来作为最终的请求方法的headers 
# s.headers.update({'x-test': 'true'}) 
# # 发送请求，这里没有设置auth会默认使用session对象的auth属性，这里的headers属性会与session对象的headers属性合并 
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'}) 
# # 查看发送请求的请求头 
# r.request.headers

import requests
import time,os,re,json

S=requests.Session()

old_headers='''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Host: ip.zdaye.com
Pragma: no-cache
Referer: http://ip.zdaye.com/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36
'''
def headers_format(headers):
    # sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
    new_headers=re.sub(r'(.*): (.*)',r'"\1":"\2",',headers)
    new_headers=new_headers.strip()[0:-1]
    new_headers='{'+new_headers+'}'
    new_headers=json.loads(new_headers)
    return new_headers
headers=headers_format(old_headers)
#以上处理了headers部分

url='http://ip.zdaye.com/'
html=S.get(url,headers=headers)
html=S.get(url,headers=headers)

cookies = html.cookies
print('; '.join(['='.join(item) for item in cookies.items()]))
# print(html.content.decode('gbk'))
# html.encoding=html.apparent_encoding
html=html.content
html=html.decode('gbk') 
# html=html.text
print(html)



