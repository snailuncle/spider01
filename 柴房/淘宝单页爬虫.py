import requests
import re
import json
from lxml import html
# url="https://s.taobao.com/search?q=python%E7%88%AC%E8%99%AB&imgfile=&js=1&stats_click=seJJarch_radio_all%3A1&initiative_id=staobaoz_20180317&ie=utf8"
url="https://s.taobao.com/search?q=python爬虫"
# url="https://s.taobao.com/search?q=python%E7%88%AC%E8%99%AB&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180317&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=88"
r=requests.get(url)
# r.encoding=r.apparent_encoding
r.raise_for_status
g_page_config=re.search(r"(?<=g_page_config = ).+(?=;\s+g_srp_loadCss\(\))",r.text,re.S|re.I)
with open('淘宝实际网页.txt','wb') as f:
    f.write(r.content)
json_str=g_page_config.group()
with open('正则匹配的网页信息.txt','w') as f:
    f.write(json_str)
dict_info=json.loads(json_str)
list_info=dict_info['mods']['itemlist']['data']['auctions']
for one_info in list_info:
    detail_dict={
        'title':one_info['title'],
        'view_price':one_info['view_price'],
        'view_sales':one_info['view_sales'],
        'nick':one_info['nick'],
        'item_loc':one_info['item_loc']        
    }
    print(detail_dict)  


