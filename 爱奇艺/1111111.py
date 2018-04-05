
#-*-coding=utf-8-*-
import sys,os
import requests
from lxml import etree
import subprocess
session = requests.Session()
# def getContent(url):
#     # url='http://www.iqiyi.com/v_19rrkwcx6w.html'
#     try:
#         ret = requests.get(url)
#         ret.encoding='utf-8'
#     # except Exception,e:
#     except:
#         # print e
#         return None
#     if ret.status_code==200:
#         return ret.text
#     else:
#         return None

# def getUrl():
#     url='http://www.iqiyi.com/v_19rrkwcx6w.html'
#     url2='http://www.iqiyi.com/v_19rrl2td7g.html' # 31-61
#     content = getContent(url)
#     if not content:
#         print ("network issue, retry")
#         exit(0)
#     root = etree.HTML(content,parser=etree.HTMLParser(encoding='utf-8'))
#     elements=root.xpath('//div[@data-current-count="1"]//li')
#     for items in elements:
#         url_item=items.xpath('.//a/@href')[0]
#         song_url = url_item.replace('//','')
#         song_url=song_url.strip()
#         print(song_url)
#         # name=items.xpath('.//span[@class="item-num"]/text()')[0]
#         s1=items.xpath('.//span[@class="item-num"]/text()')[0].encode('utf-8').strip().decode('utf-8')
#         s2=items.xpath('.//span[@class="item-txt"]/text()')[0].encode('utf-8').strip().decode('utf-8')
#         print(s1,"********",s2)
#         name=s1+s2+'.mp4'
#         name= '儿歌多多 '+name
# #         name=name.decode('utf-8')
#         filename=os.path.join(os.getcwd(),name)
#         print (filename)
#         if os.path.exists(filename):
#             continue
target_url = 'http://60.221.213.24/netcncallcnc.inter.iqiyi.com/videos/v0/20160202/2b/67/a05e4d684ddc19857e9d8e82b70a7734.f4v?key=0f2bef16b30380d0d8fb04ee3c365ff04&dis_k=0264ca547c1b45a512aed3969fcde99a&dis_t=1522933578&src=iqiyi.com&uuid=3cdd6f3e-5ac61f4a-15d&rn=1522933576924&qd_ip=3cdd6f3e&qd_stert=3601330&qd_k=1f75b23fa625f8ddf8501a4d0896141a&qd_vipdyn=0&qd_tm=1522933086170&qd_aid=202321601&cross-domain=1&pv=0.1&qd_src=01010031010000000000&qd_tvid=372295700&qypid=372295700_02020031010000000000&qd_p=3cdd6f3e&pri_idc=netcnc_cnc&tm=1522933085397&qd_index=11&qd_vip=0&qd_uid=2180295461&k_uid=&qd_vipres=0&qyid=5ff9138dcdd0f54a84833b08506d82b9&range=6099968-17252351&wshc_tag=0&wsts_tag=5ac61f4a&wsid_tag=3cdd6f3e&wsiphost=ipdbm'
song_url=target_url
p=subprocess.Popen('you-get -d --format=HD {}'.format(song_url),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
output,error = p.communicate()
print(output.decode('utf-8'))
print(error)
p.wait()

