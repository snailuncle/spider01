import http.cookiejar as HC
from bs4 import BeautifulSoup
import json
import requests
import lxml
from lxml import etree
import sys
import re
import time

url="http://xz.meituan.com"
# 将headers添加引号
# ^([-\w]+?): ([\w=.;%\-:+/*(), ]+)(?: $|$)
# '$1':'$2',
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'xz.meituan.com',
    'Referer':'http://xz.meituan.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko),Chrome/65.0.3325.32 Safari/537.36',
    'Content-Type':'text/html; charset=utf-8'
}



#获取分类链接,list:  美食,电影
def get_start_links(url):
    html=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html,'lxml')
    div=soup.find('div',class_='category-nav-content-wrapper')
    links=[sub_link.find('span').find('span').find('a')['href'] for sub_link in div.find('ul').find_all('li')] 
    return links
    # ['http://xz.meituan.com/meishi/', 'http://waimai.meituan.com', 'http://hotel.meituan.com', 'http://www.zhenguo.com/?phx_wake_up_type=mtpc_category&phx_wake_up_source=nav', 'http://maoyan.com/films?showType=1', 'http://www.meituan.com/iflight/', 'http://xz.meituan.com/xiuxianyule/', 'http://xz.meituan.com/shenghuo/', 'http://xz.meituan.com/jiankangliren/', 'http://xz.meituan.com/jiehun/', 'http://xz.meituan.com/qinzi/', 'http://xz.meituan.com/yundongjianshen/', 'http://xz.meituan.com/jiazhuang/', 'http://xz.meituan.com/jiaoyupeixun/', 'http://xz.meituan.com/yiliao/', 'http://xz.meituan.com/xiuxianyule/c234/']


# 在商店列表页  获取店名列表
def get_store_name(url):
    print(url)
    html=requests.get(url,headers=headers)
    cookies=html.cookies
    html=html.text
    pattern = re.compile(r"(?<=window._appState = ).+?(?=;</script>)",re.S)
    data=re.search(pattern,html).group(0)
    dict1=json.loads(data)
    store_list=dict1['poiLists']['poiInfos']
    store_detail_list=[]
    for store in store_list:
        dict2={
            "name":store['title'],
            'ID':store['poiId']
        }
        store_detail_list.append(dict2)
    return store_detail_list,cookies
    # [{'name': '莲年有鱼碳烤鱼（牌楼店）', 'ID': 4042134}, {'name': '欢乐思碧客（彭城一号店）', 'ID': 6730869}, {'name': '泰好吃·泰国餐厅', 'ID': 42560531}, {'name': '傣妹火锅（中山北路店）', 'ID': 1555520}, {'name': '哆来咪火锅烤肉自助', 'ID': 23282}, {'name': '金诺郎海鲜自助烤肉火锅', 'ID': 41561274}, {'name': '韩食刻·芝士火锅', 'ID': 4184850}, {'name': '巴厘岛海鲜自助', 'ID': 5921390}, {'name': '妯娌老鸭粉丝馆（悠沃店）', 'ID': 2418274}, {'name': '艾尚客自助餐厅', 'ID': 6615546}, {'name': '黄记煌三汁焖锅（云龙万达店）', 'ID': 6824666}, {'name': '张记炒货', 'ID': 51336155}, {'name': '阿郎山烤肉美食超市', 'ID': 42635}, {'name': '二妮菜煎饼（万达百货店）', 'ID': 4777897}, {'name': '映像徐州（滨湖店）', 'ID': 41209720}, {'name': '汉丽轩烤肉（福泰隆店）', 'ID': 6437218}, {'name': '刘先生的肉肉（万达百货店）', 'ID': 6716646}, {'name': '欢乐思碧客麻辣香锅（贾汪百大店）', 'ID': 4623950}, {'name': '牙缝烧烤俱乐部', 'ID': 41748756}, {'name': '二妮菜煎饼（新区同昌店）', 'ID': 40136302}, {'name': '欢乐牧场烧烤涮自助餐厅（万达百货店）', 'ID': 5840242}, {'name': '麦可麦客MOCO MARK（金地店）', 'ID': 5548690}, {'name': '麦咔兹（贾汪百大店）', 'ID': 50359238}, {'name': '艾大米（沃尔玛店）', 'ID': 6008324}, {'name': '比格自助比萨（万达百货店）', 'ID': 5750144}, {'name': '永康糕点（夹河街店）', 'ID': 29026}, {'name': '欢乐牧场烧烤涮时尚自助餐厅', 'ID': 41604132}, {'name': '东淮西川（万达百货店）', 'ID': 4755723}, {'name': '欢乐思碧客麻辣香锅（恒盛广场店）', 'ID': 40758973}, {'name': '冠林蛋糕（香城店）', 'ID': 2075390}, {'name': '蜜忆甜品（金地商都店）', 'ID': 2494575}, {'name': '正宗台湾脆皮玉米（沛县总店）', 'ID': 50308218}]

def get_store_detail(url,cookies):
    # 3 meishi
    # 4 ID
    ref_list=url.split("/")
    pattern = re.compile(r"%s"%ref_list[4])
    ref=re.search(pattern,url).group(0)
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'xz.meituan.com',
        'Referer':ref,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
    }
    # url=https://www.meituan.com/cate/80274/       星美国际影商城      特殊网址,正则匹配失败
    # url="https://www.meituan.com/meishi/80274/"
    html=requests.get(url,headers=headers,cookies=cookies).text
    # save_text(url+"\n\n"+html)
    #------------------------具体某个商店的信息----------------------------------------------------------
    # pattern = re.compile(r"(?<=script>window._appState = ).*?(?=,\"extraInfos)|(?<=<script>window.AppData = ).*?(?=,\"headIcon\":\"http)",re.I)
    pattern = re.compile(r"(?<=script>window._appState = ).*?(?=,\"avgPrice)|(?<=<script>window.AppData = ).*?(?=,\"brandId)",re.I)
    store_detail_info=re.search(pattern,html).group(0)+"}}"
    save_text_mode_w(store_detail_info)
    #-------------------------商店的所有信息包括经纬度--------------------------------
    store_detail_info_dict=json.loads(store_detail_info)
    info=store_detail_info_dict['detailInfo'] if 'detailInfo' in store_detail_info_dict.keys() else store_detail_info_dict['poiInfo']
    # "lng":117.249531,"lat":34.249628,
    dict3={
        'name':info['name'],
        'address':info['address'],
        'phone':info['phone'],
        'open_time':info['openTime'],
        'longitude':info['longitude'] if 'longitude' in info.keys() else info['lng'],
        'latitude':info['latitude'] if 'latitude' in info.keys() else info['lat']
    }
    info_text=json.dumps(dict3,ensure_ascii=False)
    print(info_text)
    # sys.exit()
    with open('meituan_stores.txt', 'a',encoding='utf-8') as f:
        f.write(info_text)
        f.write("\n\n")

def save_text_mode_w(text):
    with open('meituan.txt','w',encoding='utf-8') as f:
        f.write(text)




def main():
    start_url_list=get_start_links(url+"/")
    for link in start_url_list:
        print(link)
        store_list,cookies=get_store_name(link)
        for store in store_list:
            #这是第一页,爬完之后该翻页了
            print(store)
            store_url=link+str(store['ID'])+"/"
            get_store_detail(store_url,cookies)
            # get_store_detail(store['ID'])
            time.sleep(0.01)
        
        for i in range(2,66):
            # http://xz.meituan.com/meishi/
            # http://xz.meituan.com/meishi/pn2/
            print('********第%d页*********'%i)
            next_url=link+'pn'+str(i)+"/"
            try:
                store_list,cookies=get_store_name(next_url)
                with open('meituan_stores.txt', 'a',encoding='utf-8') as f:
                    f.write('********第%d页*********'%i)
                    f.write(next_url)
                    f.write(str(store_list))
                    f.write("\n\n")
                if len(store_list)==0:
                    print("zhixing******break")
                    break
                for store in store_list:
                    store_url=link+str(store['ID'])+"/"
                    with open('meituan_stores.txt', 'a',encoding='utf-8') as f:
                        f.write(store_url)
                        f.write("\n\n")                    
                    get_store_detail(store_url,cookies)  
                    time.sleep(0.1)    
            except Exception as e:
                print(e)
                break                 






if __name__=='__main__':
    main()
