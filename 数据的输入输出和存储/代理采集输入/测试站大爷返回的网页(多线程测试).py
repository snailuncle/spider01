import requests
import time,os,re,json,sys,random
from 代理 import proxy_get
from fake_useragent import UserAgent
import traceback
from multiprocessing import Pool
import multiprocessing
ua=UserAgent()

# print("UA: = "+rnd_ua)

# sys.exit()
# GET / HTTP/1.1
# Host: ip.zdaye.com

def headers_format():
    rnd_ua=ua.random
    old_headers='''
    Host: ip.zdaye.com
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: {}
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    '''.format(rnd_ua)

    # sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
    new_headers=re.sub(r'([^ ]*?): *(.+)',r'"\1":"\2",',old_headers)
    # print(old_headers)
    # print(new_headers)
    print('%'*99)
    time.sleep(3)
    new_headers=new_headers.strip()[0:-1]
    new_headers='{'+new_headers+'}'
    new_headers=json.loads(new_headers)
    print(new_headers)
    return new_headers

def get_rnd_headers():
    return headers_format()

#以上处理了headers部分


# print(headers)


# proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
# requests.get('http://example.org', proxies=proxies)

# proxies=proxy_get()
def get_rnd_proxies(rnd_num):
    list1=json_proxies1['msg']
    proxies=list1[rnd_num]
    proxies="{{'http':'http://{ip}:{port}'}}".format(**proxies)
    # proxies={'http':'http://115.207.82.124:39598'}
    proxies=eval(proxies)

    print('proxies=',proxies)
    return proxies



def get_content_from_url(url,rnd_num):
    headers=get_rnd_headers()
    proxies=get_rnd_proxies(rnd_num)
    if url=='http://httpbin.org/ip':
        print('ip地址测试')
        r=requests.get(url,timeout=5,proxies=proxies)
    else:
        r=requests.get(url,headers=headers,timeout=6,proxies=proxies)
    # r=requests.get(url,timeout=16,proxies=proxies)
    r.encoding='gbk'
    print('*'*50)
    print(r.text)

    lock = multiprocessing.Lock()
    lock.acquire()
    with open(r'D:\spider01\数据的输入输出和存储\proxies.txt','a') as f:
        f.write(str(proxies)+'\n\n')
    lock.release()



json_proxies1={"code":"0","msg":[{"port":"38397","ip":"117.69.200.206"},{"port":"45190","ip":"36.248.133.115"},{"port":"28719","ip":"27.204.42.166"},{"port":"29154","ip":"36.26.152.163"},{"port":"33338","ip":"183.164.239.215"},{"port":"21665","ip":"36.250.156.111"},{"port":"44508","ip":"125.105.111.7"},{"port":"39322","ip":"175.42.128.187"},{"port":"35857","ip":"182.126.11.104"},{"port":"39598","ip":"115.207.82.124"},{"port":"48398","ip":"123.8.250.5"},{"port":"42611","ip":"171.14.211.217"},{"port":"20376","ip":"1.199.195.130"},{"port":"20795","ip":"175.44.108.137"},{"port":"49446","ip":"175.44.109.61"},{"port":"34788","ip":"27.204.83.227"},{"port":"27370","ip":"36.248.132.115"},{"port":"32779","ip":"61.162.241.104"},{"port":"36882","ip":"182.126.8.176"},{"port":"32401","ip":"117.28.161.88"},{"port":"43530","ip":"117.25.191.114"},{"port":"30127","ip":"112.111.77.82"},{"port":"29328","ip":"175.44.109.64"},{"port":"28005","ip":"125.105.104.112"},{"port":"49317","ip":"182.120.202.120"},{"port":"39952","ip":"182.120.202.107"},{"port":"32734","ip":"117.28.145.66"},{"port":"36913","ip":"123.134.221.227"},{"port":"26509","ip":"125.106.248.244"},{"port":"43676","ip":"220.249.149.38"},{"port":"41844","ip":"175.43.156.4"},{"port":"28978","ip":"123.149.162.134"},{"port":"41445","ip":"175.43.131.114"},{"port":"36192","ip":"123.134.219.113"},{"port":"30598","ip":"218.104.255.4"},{"port":"40972","ip":"123.55.3.37"},{"port":"32809","ip":"113.121.242.197"},{"port":"26777","ip":"220.249.149.43"},{"port":"45625","ip":"27.204.85.203"},{"port":"24953","ip":"36.248.132.165"},{"port":"45848","ip":"117.69.200.234"},{"port":"32042","ip":"120.39.118.195"},{"port":"41082","ip":"112.111.217.86"},{"port":"34656","ip":"125.106.249.150"},{"port":"37678","ip":"175.43.151.146"},{"port":"37955","ip":"100.69.197.68"},{"port":"36730","ip":"175.43.32.43"},{"port":"20229","ip":"125.106.21.33"},{"port":"31176","ip":"175.43.58.52"},{"port":"44474","ip":"218.73.134.176"},{"port":"33386","ip":"182.120.244.249"},{"port":"35746","ip":"123.55.2.158"},{"port":"26649","ip":"183.164.238.169"},{"port":"44911","ip":"125.106.21.97"},{"port":"27717","ip":"114.219.122.103"},{"port":"22428","ip":"115.207.39.115"},{"port":"48720","ip":"36.250.156.72"},{"port":"28697","ip":"123.10.65.188"},{"port":"47660","ip":"123.55.1.117"},{"port":"21216","ip":"114.218.33.74"},{"port":"31366","ip":"113.121.243.24"},{"port":"20434","ip":"182.126.52.49"},{"port":"23279","ip":"113.121.240.48"},{"port":"31617","ip":"218.66.146.165"},{"port":"29392","ip":"123.149.163.172"},{"port":"49590","ip":"175.44.109.21"},{"port":"37456","ip":"49.72.156.244"},{"port":"31316","ip":"117.57.90.228"},{"port":"41544","ip":"175.43.179.63"},{"port":"20632","ip":"175.42.158.83"},{"port":"31605","ip":"218.66.144.136"},{"port":"36740","ip":"36.248.132.81"},{"port":"23584","ip":"175.43.59.41"},{"port":"25469","ip":"218.66.144.85"},{"port":"40545","ip":"36.248.132.111"},{"port":"25126","ip":"49.85.3.80"},{"port":"25267","ip":"175.42.122.88"},{"port":"38709","ip":"58.22.177.192"},{"port":"42066","ip":"36.248.133.143"},{"port":"38588","ip":"27.204.127.122"},{"port":"36240","ip":"36.250.156.40"},{"port":"40225","ip":"115.221.119.88"},{"port":"34145","ip":"49.85.3.33"},{"port":"29409","ip":"175.42.128.172"},{"port":"38825","ip":"27.204.64.152"},{"port":"30329","ip":"125.121.172.122"},{"port":"23186","ip":"175.42.123.210"},{"port":"32476","ip":"115.210.79.251"},{"port":"40910","ip":"115.221.120.222"},{"port":"37503","ip":"183.150.165.53"},{"port":"31004","ip":"36.248.129.56"},{"port":"26085","ip":"123.134.218.147"},{"port":"47063","ip":"175.44.108.185"},{"port":"43858","ip":"175.42.128.207"},{"port":"40254","ip":"27.204.120.25"},{"port":"30944","ip":"218.73.137.53"},{"port":"42255","ip":"123.53.134.56"},{"port":"32726","ip":"36.248.132.137"},{"port":"45686","ip":"27.204.113.205"},{"port":"42185","ip":"125.109.197.93"},{"port":"34785","ip":"123.163.21.106"},{"port":"20144","ip":"182.126.14.92"},{"port":"46900","ip":"180.115.100.18"},{"port":"48010","ip":"117.69.200.223"},{"port":"36543","ip":"175.42.129.181"},{"port":"37358","ip":"36.250.156.60"},{"port":"31877","ip":"175.43.142.96"},{"port":"33601","ip":"115.48.95.38"},{"port":"49593","ip":"123.55.69.70"},{"port":"31835","ip":"115.48.85.231"}]}

def test_proxy(i,url):
    try:
        print('*'*55)
        rnd_num=i
        get_content_from_url(url,rnd_num)
        print('O'*66)

    except Exception as e:
        print('!'*55)
        print(e)
        traceback.print_exc()

if __name__=='__main__':
    # url='http://ip.zdaye.com/'
    url='http://httpbin.org/ip'
    pool = Pool(4)
    while True:
        for i in range(54,len(json_proxies1['msg'])-1):
            time.sleep(0.1)
            print(i)
            pool.apply_async(test_proxy, args=(i,url))
        pool.close()
        pool.join()
        break



# pool = Pool(4)
# print "Son process is started"
# for x in range(0, 10):
#     pool.apply_async(son_process, args=('son_%d'%x,))
# pool.close()
# print "Mark"
# pool.join()                

            