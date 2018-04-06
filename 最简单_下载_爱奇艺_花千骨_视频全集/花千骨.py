import requests
import re,os,time,json,sys
import subprocess as sp
#运行本脚本至少等待5分钟
#视网络情况和电脑等级而定.
#不加UA不返回正确信息
old_headers='''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Host: www.iqiyi.com
Referer: http://www.iqiyi.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36
'''
def headers_format(headers):
    # sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
    new_headers=re.sub(r'(.*): (.*)',r'"\1":"\2",',headers)
    new_headers=new_headers.strip()[0:-1]
    new_headers='{'+new_headers+'}'
    new_headers=json.loads(new_headers)
    return new_headers
headers=headers_format(old_headers)
#以上处理了headers部分




#返回花千骨1-30集的url链接
def huaqiangu_urls():
    print('enter huaqiangu_urls()')
    #花千骨第一集链接
    url='http://www.iqiyi.com/v_19rroheauw.html'
    print(headers)
    html=requests.get(url,headers=headers,timeout=6)
    html.encoding=html.apparent_encoding
    html_text=html.text
    print(html_text)
    #从网页源代码中提取url链接
    #分为两步
    #第一步,提取1-30集的综合信息
    pattern=r'(?<=mixinVideos":\[).*?(?=\],"page":1)'
    string=html_text
    video_info=re.search(pattern,string)
    video_info=video_info.group()
    #第二步,提取1-30集的url链接
    pattern=r'(?<="url":")http://www.iqiyi.com/\w*?.html(?=","playCoun)'
    string=video_info
    urls=re.findall(pattern,string)
    print('return \n huaqiangu_urls=',str(urls))
    return list(urls)

def video_download(url):
    # url='http://www.iqiyi.com/v_19rroheauw.html'
    # url='http://www.iqiyi.com/v_19rrnsr5zw.html'
    try:
        #提取视频名字
        cmd='you-get -i "%s"  '%url
        #执行命令
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True) 
        #获得返回结果并解码
        out = p.stdout.read().decode("utf-8")
        name=re.findall(r"(?<=title:).*",out)[0].strip()
        print(name)
        # 使用--output-dir/-o 设定路径, --output-filename/-O 设定输出文件名:
        # $ you-get -o ~/Videos -O zoo.webm 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
        cmd='you-get --format=LD -o D:/spider01/最简单_下载_爱奇艺_花千骨_视频全集 -O %s  "%s"  '%(name,url)
        # you-get --format=LD [URL]
        #执行命令
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, shell=True) 
        #获得返回结果并解码
        # out = p.stdout.read().decode("utf-8")
        line = p.stdout.readline()
        while line:
            line=line.decode("utf-8")
            print(line)
            line = p.stdout.readline()
    except Exception as e:
        print(e)

# import subprocess
# subp=subprocess.Popen('python -u /tmp/test.py',shell=True,stdout=subprocess.PIPE)
# while subp.poll()==None:
#     print stdout.readline()
# print subp.returncode


urls=huaqiangu_urls()
for url in urls:
    print(url)
    video_download(url)
