import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
weibo = client['weibo']
comment_shengmengc = weibo['comment_shengmengc']

headers = {
    "Cookies":'_T_WM=040e9cc680ab0ab1c1e07e8bac4b1318; SCF=ApEUyfHcHBch9XwUjgcYsLdDzisBMd4uYaQy65RsYUByK-N4ovJxIlRDdHwaOHRr3tZBZNv-LVdGgndPrAd09HM.; SUB=_2A253qwR3DeRhGeRO6FUW8CnNzDuIHXVVV6w_rDV6PUJbkdANLXfXkW1NUGxRMT8jSM-3iFZhwkxscDi8UB0pSlJV; SUHB=05i7QX7RM69ooG',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

url_comment = ['http://m.weibo.cn/api/comments/show?id=4060977869675098&page={}'.format(str(i)) for i in range(0,1000)]
def get_comment(url):
    wb_data = requests.get(url,headers=headers).text
    data_comment = json.loads(wb_data)
    try:
        datas = data_comment['data']
        for data in datas:
            comment = {"comment":data.get("text")}
            comment_shengmengc.insert_one(comment)
    except KeyError:
        pass
for url in url_comment:
    get_comment(url)
    time.sleep(2)
