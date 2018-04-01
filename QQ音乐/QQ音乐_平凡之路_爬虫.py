#本文更新于2018 04 01

######下面是我的分析过程,后面分析的很烦躁,就不想写了,自己看吧
######思路大概是下面这样的
#####但是后来抓链接的时候,开始能用,
#####后来居然失效了,
#####人就烦躁了,又分析了一次才抓到可用的链接地址
####实在不想打字了,
#####就算开始错了,思路是对的,总是可以抓到的.

#####总体思路==============模仿人请求网页的过程

# 目标爬取QQ音乐下载地址
#用例:华晨宇改造的<平凡之路>

#首先打开ＱＱ音乐搜索＜平凡之路＞，第一首歌就是华晨宇改造的＜平凡之路＞
#打开这首歌的播放页面
#按F12  查看这首歌的播放链接
#在elements标签下面
#有两个链接都可以播放<平凡之路>这首歌
#我们选择的是第一个链接
#http://dl.stream.qqmusic.qq.com/C400003suD9L2tvMnZ.m4a?vkey=76F4A43A2D84A18CEC27BDB8B507B855E3066482B8398318637EB8F563F1784B074F54D7559F8147A3B5A4FB52C772A8C9A3F1E128D0F317&guid=8148305384&uin=0&fromtag=66

#我们解析一下这个链接的格式,
# http://dl.stream.qqmusic.qq.com/
# C400003suD9L2tvMnZ.m4a?
# vkey=76F4A43A2D84A18CEC27BDB8B507B855E3066482B8398318637EB8F563F1784B074F54D7559F8147A3B5A4FB52C772A8C9A3F1E128D0F317
# &guid=8148305384
# &uin=0
# &fromtag=66

# 你看到什么了吗,
#反正我是没看到
#这里我们采用对比的方法
#再找一首歌
#比如朴树的<平凡之路>

#同样的方法,得到朴树的<平凡之路>的链接
#下面是两个链接,我们对比一下
#华晨宇
# http://dl.stream.qqmusic.qq.com/
# C400003suD9L2tvMnZ.m4a?
# vkey=76F4A43A2D84A18CEC27BDB8B507B855E3066482B8398318637EB8F563F1784B074F54D7559F8147A3B5A4FB52C772A8C9A3F1E128D0F317
# &guid=8148305384
# &uin=0
# &fromtag=66

#朴树
# http://dl.stream.qqmusic.qq.com/
# C40000020yc41KtWj2.m4a?
# vkey=9D3BB142671E9164DC1D3A63E00FD335E05FFE55FB483E03182D6EB7FEB2B342DB082F717B1EA945ADBFE386DC0C2C75F57B713B297A7CA0
# &guid=8148305384
# &uin=0
# &fromtag=66

#经测试发现  后面两个字段删掉,同样可以播放歌曲
#那么我们当前要提取的信息是
#m4a编号
#vkey编号
#guid编号
#一首歌干嘛要这么多编号啊,猜一猜是不是
#歌名,歌手,歌曲文件编号?
#我瞎猜的.

#可以看到guid是一样的,
#那么guid就是歌名,只不过用编号代替


#猜测一下这三个字段
# guid因为一样,应该可以从搜索页面获得
# m4a大概是歌手的名字,应该也能从搜索页面获得
# vkey大概是mp3文件的编号,因为太长了应该是点击播放的时候才会去服务器上提取
#以上纯属虚构,雷同巧合.

#什么,你问我,为什么这么猜?
#你搜索歌曲的时候难道看不见,歌手和歌曲的名字吗???

#现在我们去搜索<平凡之路>的网页源代码看看
#很不幸,网页源代码没有,
#guid mua vkey三个字段都没有

#祭出神器F12, 刷新页面(平凡之路的搜索页面)
#你问我为什么?
#因为我搜索以后,页面上展示了,歌曲的名字和歌手的名字.
#当然了,这些都是猜测,碰运气.

#在network/js下面,可以找到这个请求
#https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61002769177010133&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%B9%B3%E5%87%A1%E4%B9%8B%E8%B7%AF&g_tk=5381&jsonpCallback=MusicJsonCallback6295537215356191&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0
#点击它,可以再右边的preview看到<平凡之路>
#查看他的响应
#返回的是一个json
#往下翻几行,能看到华晨宇,朴树等歌手的名字
#但是,还是没有我们想要的任何字段
#guid vkey m4a




#但是仔细再看一下
#在json路径JSON.data.song.list[0].file.strMediaMid
#有一个strMediaMid键
#键值是"003suD9L2tvMnZ"
#这个是华晨宇的m4a字段
#######下面的是上面的部分信息########
#同样的方法,得到朴树的<平凡之路>的链接
#下面是两个链接,我们对比一下
#华晨宇
# http://dl.stream.qqmusic.qq.com/
# C400003suD9L2tvMnZ.m4a?
# vkey=76F4A43A2D84A18CEC27BDB8B507B855E3066482B8398318637EB8F563F1784B074F54D7559F8147A3B5A4FB52C772A8C9A3F1E128D0F317
# &guid=8148305384
# &uin=0
# &fromtag=66

#朴树
# http://dl.stream.qqmusic.qq.com/
# C40000020yc41KtWj2.m4a?
# vkey=9D3BB142671E9164DC1D3A63E00FD335E05FFE55FB483E03182D6EB7FEB2B342DB082F717B1EA945ADBFE386DC0C2C75F57B713B297A7CA0
# &guid=8148305384
# &uin=0
# &fromtag=66

#目前只找到了m4a的字段
#是从这个json中提取出来的
#这个json是从某个链接提取出来的
#这个链接是一个get
#https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61002769177010133&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%B9%B3%E5%87%A1%E4%B9%8B%E8%B7%AF&g_tk=5381&jsonpCallback=MusicJsonCallback6295537215356191&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

#这个json链接的构造
#&w之后是平凡之路,四个字
#url解码
#https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61002769177010133&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=平凡之路&g_tk=5381&jsonpCallback=MusicJsonCallback6295537215356191&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0

#看看字段能不能删掉一些,实在是太长了
#你问删哪个?
#我哪里知道,一个一个试,
#返回的json不一样的话
#就是不能删掉的字段
#下面是一个一个测试过后,精简的链接
#https://c.y.qq.com/soso/fcgi-bin/client_search_cp?new_json=1&remoteplace=txt.yqq.song&aggr=1&cr=1&w=%E5%B9%B3%E5%87%A1%E4%B9%8B%E8%B7%AF
#https://c.y.qq.com/soso/fcgi-bin/client_search_cp?new_json=1&remoteplace=txt.yqq.song&aggr=1&cr=1&w=%E5%B9%B3%E5%87%A1%E4%B9%8B%E8%B7%AF
#
#&w后面是                  平凡之路

#我们再搜索一下其他歌曲,看与该链接有哪里不一样
#经对比发现
#只有一个不同,那就是我们搜索的歌名
#即&w之后的字符

import requests
import re
import json
import os
import time
from lxml import etree
from urllib.parse import quote

#提取歌曲id
song_name_original="平凡之路"
song_name=quote(song_name_original)
url="https://c.y.qq.com/soso/fcgi-bin/client_search_cp?new_json=1&remoteplace=txt.yqq.song&aggr=1&cr=1&w=%s"%(song_name)
print(url)
html=requests.get(url).text
html=re.search("(?<=callback\().*(?=\))", html)
html=html.group(0)
html_json=json.loads(html)
song_mid=html_json['data']['song']['list'][0]['file']['media_mid']
print(song_mid)


#华晨宇         
# http://dl.stream.qqmusic.qq.com/
# C400      003suD9L2tvMnZ.m4a?
# vkey=76F4A43A2D84A18CEC27BDB8B507B855E3066482B8398318637EB8F563F1784B074F54D7559F8147A3B5A4FB52C772A8C9A3F1E128D0F317
# &guid=8148305384
# &uin=0
# &fromtag=66

url='https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songmid=%s&format=jsonp'%(song_mid)
html=requests.get(url).text
html=re.search("(?<=\().*(?=\))", html)
html=html.group(0)
html_json=json.loads(html)
# C400003suD9L2tvMnZ

id=html_json['data'][0]['id']
print(id)
url=html_json['url'][str(id)]
print(url)

#写入mp3
html=requests.get('http://%s'%url).content
with open(r'D:/%s.mp3'%(song_name_original),'wb') as f:
    f.write(html)







