#默认爬取指定商品50页
import re
import requests
url='https://s.taobao.com/search'
payload={'q':'python爬虫','s':'0','ie':'utf8'}
file=open('淘宝翻页爬取.txt','w',encoding='utf-8')

for k in range(0,50):
    payload['s']=44*k
    resp=requests.get(url,params=payload)
    print(str(k)+resp.url)
    resp.encoding='utf-8'
    raw_title = re.findall(r'"raw_title":"([^"]+)"',resp.text,re.I)
    view_price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I)
    view_sales = re.findall(r'"view_sales":"([^"]+)"',resp.text,re.I)
    nick = re.findall(r'"nick":"([^"]+)"',resp.text,re.I)
    item_loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
    x=len(raw_title)
    for i in range(0,x):
        info=str(k*44+i+1) + '    title: '+raw_title[i] +'    price: '+view_price[i] +'    sale: '+view_sales[i] +'    nick: '+nick[i] +'    location: '+item_loc[i]
        info=info+'\n\n'
        file.write(info)

file.close()

