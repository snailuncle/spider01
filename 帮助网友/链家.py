import requests
import re
from lxml import etree
def get_one_page(url):
    response=requests.get(url,headers={'user-agent':'Mozilla/5.0'})
    if response.status_code==200:
        return response.text
    return "错误"
def parse_one_page(html):
    # pattern = re.compile(
    #     '<li class="clear".*?<div class="title".*?data-s1>(.*?)</a>.*?</li>',
    #     re.S)
    # items=re.findall(pattern, html)
    # print(items)
    selector=etree.HTML(html)
    xpath_str="//ul[@class='sellListContent']/li[@class='clear']/div[@class='info clear']/div[@class='title']/a/text()"
    content=selector.xpath(xpath_str)
    for each in content:
        print(each)

def main():
    url='https://sz.lianjia.com/ershoufang/'
    html=get_one_page(url)
    parse_one_page(html)

main()
