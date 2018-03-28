# 输入在谷歌浏览器复制的headers
# 输出爬虫可用的headers
# 默认不包含cookie
# 参数ck设置为1表示包含cookie
import re
with_cookie_headers='''
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'BAIDUIk3SLVN4HKm; H1080_22072; sugstore=1',
'Host':'www.baidu.com',
'Referer':'https://www.baidu.com/link?url=SGQgmZq9pP32GkKsemy9m_PUNZcMjQTGbe7qSEzdU3i&wd=&eqid=9559b67e0005d18d000000025abaed4c',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36',
'''

def del_cookie(with_cookie_headers):
    pattern = re.compile(r"'Cookie':'[^']+',\n")  
    del_cookie=pattern.sub('',with_cookie_headers)
    del_cookie=del_cookie[0:-2]
    print(del_cookie)
    return del_cookie

del_cookie(with_cookie_headers)


