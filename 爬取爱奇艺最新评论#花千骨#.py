import requests
from lxml import etree
import json
import time

def get_one_page(url):
    html=requests.get(url).text
    dict_obj=json.loads(html)
    comment_list=dict_obj['data']['feeds']
    for each in comment_list:
        comment={
            'name':each['name'],
            'description':each['description'],
            'releaseDate':timestamp_to_time(each['releaseDate'])
        }
        for key,value in comment.items():
            print(key+':'+value)
        print('')

def timestamp_to_time(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

def main():
    url='http://api-t.iqiyi.com/feed/get_feeds?&agenttype=118&wallId=200091447'
    get_one_page(url)

if __name__=='__main__':
    main()
