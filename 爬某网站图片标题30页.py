import requests
from lxml import etree
# url='http://www.doooor.com/thread-10958-1.html'

def get_one_page(url):
    html=requests.get(url).text
    # print(html)
    selector=etree.HTML(html)
    xpath_str="//li[@class='scitem scitemimage']/div[@class='simgbody simgh cl']/a[@class='simgtitle']/text()"
    content=selector.xpath(xpath_str)
    # print(content)
    for each in content:
        print(each)


# http://www.doooor.com/p2.html
    

def main():
    index_url='http://www.doooor.com/'
    get_one_page(index_url)
    for i in range(2,30):
        url=index_url+"p"+str(i)+".html"
        print(url)
        get_one_page(url)

if __name__=='__main__':
    main()
