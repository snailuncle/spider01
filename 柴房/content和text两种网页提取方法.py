import requests
from lxml import etree
from multiprocessing.dummy import Pool
cook={"Cokkie":"_T_WM=040e9cc680ab0ab1c1e07e8bac4b1318; TMPTOKEN=fv77tHEue09rPfyHVytwc0jWeTuiRfPIxeRb2B67aepkSY8OCEYKAJ9SDPQRG1Bb; SCF=ApEUyfHcHBchddt9XwUjgasdffacYsLsdfddDsdfasfzisBasasdffafMd4uYasdfgQy65RsYUByK-N4ovJxIlRDdHwaOHRr3tZBZNv-LVdGgndPrAd09HM.; SUB=_2A253qx1HDeRhGeRO6FUW8CnNzDuIHXVVV6MPrDV6PUJbkdAKLRXGkW1NUGxRMR7Td18VvoeCkhN6zoheWHwRbpK6; SUHB=0QS4G3Pe_4Zsj4; SSOLoginStatdae=1sdf521446167"}

url='https://weibo.cn/yuanli'

# html=requests.get(url,cookies=cook).content
html=requests.get(url,cookies=cook).text
html=bytes(bytearray(html,encoding='utf-8'))
# print(html)
# html.encoding=html.apparent_encoding
# print(html.text)
selector=etree.HTML(html)
# print(selector.xpath('string(.)'))
content=selector.xpath("//span[@class='ctt']")
# print(content)
for each in content:
    text=each.xpath('string(.)')
    b=1
    print(text)




