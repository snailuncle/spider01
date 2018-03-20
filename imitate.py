import requests
import re
from lxml import html
import os
import time
import sys


def get_atlas_info(url):

        # headers = {'Referrer Policy': 'no-referrer-when-downgrade',
        #            'Referer': url,
        #            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'}
        # try:
        #     r = requests.get(big_picture_url, headers=headers, timeout=10)


#爬取主页的所有图集的链接
    # 图集的   atlas_title  和   atlas_date
    r=requests.get(url).content
    selector=html.fromstring(r)
    atlas_titles=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[@class='title']/a")
    atlas_dates=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[2]")
    atlas_links=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[@class='title']/a/@href")
    atlas_info_list=[]
    for atlas_title,atlas_date,atlas_link in zip(atlas_titles,atlas_dates,atlas_links):
        # if atlas_link:
        #     print(str(atlas_link))
        #     atlas_link_re=re.search(r"\d+$", atlas_link.strip())
        #     http://www.mmjpg.com/mm/1275
        #     index='http://www.mmjpg.com/'
        #     if atlas_link_re:
        #         atlas_link=url+'mm/'+str(int(atlas_link_re.group(0))+15)
        atlas_info={
            'atlas_title':atlas_title.text if atlas_title is not None else '----',
            'atlas_date':atlas_date.text if atlas_date is not None else '----',
            'atlas_link':atlas_link if atlas_link is not None else '----'
        }
        print(atlas_info)
        atlas_info_list.append(atlas_info)
    print(len(atlas_info_list))
    return atlas_info_list
    # http://www.mmjpg.com/mm/1290
    # http://www.mmjpg.com/mm/1290/2

def from_url_get_xpath_result(url,xpath_str):
    r=requests.get(url).content
    selector=html.fromstring(r)
    result=selector.xpath(xpath_str)
    return result


# def download_picture(url):
#     # /html/body/div[@class='main']/div[@class='article']/div[@id='content']/a/img/@src
#     xpath_str="//div[@class='main']/div[@class='article']/div[@id='content']/a/img/@src"
#     r=from_url_get_xpath_result(url,xpath_str)
    



def get_one_atlas(url):
    #图集第一页
    #从第一页开始爬,给出终止条件,没有找到图片链接
    #构造下一页的URL
    #http://www.mmjpg.com/mm/1276                 /2
    print(url)
    print("正在下载第%d张"%1)
    save_pic(url)
    for i in range(2,6):
        time.sleep(1)
        print("正在下载第%d张"%i)
        big_picture_url=url+'/'+str(i)
        result=save_pic(big_picture_url)
        if not result:
            print('get_one_atlas Error===not save_pic(big_picture_url)==='+big_picture_url)
            break





    # atlas_titles=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[@class='title']/a")
    # atlas_dates=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[2]")
    # atlas_links=selector.xpath("//div[@class='main']/div[@class='pic']/ul/li/span[@class='title']/a/@href")


def save_pic(url):
    xpath_str="//div[@class='main']/div[@class='article']/div[@id='content']/a/img/@src"
    # xpath_str="//div[@class='article']/div[@id='content']/a/img/@src"
    pic_links=from_url_get_xpath_result(url,xpath_str)
    big_picture_url=pic_links[0] if pic_links else None
    print(pic_links)
    print(big_picture_url)
    if big_picture_url:
        print('big_picture_url is normal')
        headers = {'Referrer Policy': 'no-referrer-when-downgrade',
                   'Referer': url,
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'}
        try:
            r = requests.get(big_picture_url, headers=headers, timeout=10)
            r.raise_for_status()
        except Exception as e:
            print('save_pic : response Error')
            sys.exit()
        # r.encoding=r.apparent_encoding
        folder='D:/crawler_formal_start/pic/'
        if os.path.exists(folder) is False:
            os.mkdir(folder)
        file_name=folder+os.path.basename(big_picture_url)
        if not os.path.exists(file_name):
            try:
                with open(file_name, 'wb') as f:
                    f.write(r.content)
            except Exception as e:
                print('save_pic_error', e)
                print(url)
        else:
            print(file_name +' exists----')
        return True
    else:
        print('big_picture_url is abnormal'+url)
        return False
# path=robot+url.split('/')[-1]  
#             url=url.replace('\\','')  
#             r=requests.get(url,timeout=30)  
#             r.raise_for_status()  
#             r.encoding=r.apparent_encoding  
#             if not os.path.exists(robot):  
#                 os.makedirs(robot)  
#             if not os.path.exists(path):  
#                 with open(path,'wb') as f:  
#                     f.write(r.content)  
#                     f.close()  
#                     print(path+' 文件保存成功')  
#             else:  

# def get_page_number(num):
#     index='http://www.mmjpg.com/'
#     # http://www.mmjpg.com/home/2
#     url=index+'home/'+str(num)

#     pass

def main(url):
    #爬取主页图集信息
    atlas_info_list=get_atlas_info(url)
    print(atlas_info_list)
    #爬取单个图集
    for i in range(len(atlas_info_list)):
        print(atlas_info_list[i]['atlas_title']+'   '+atlas_info_list[i]['atlas_date'])
        link=atlas_info_list[i]['atlas_link']
        if link:
            get_one_atlas(link)
        else:
            print('atlas_link_error '+link)
            pass





if __name__=='__main__':
    index='http://www.mmjpg.com/'
    # main(index)
    # http://www.mmjpg.com/home/86
    for i in range(2,87):
        next_url=index+'home/'+str(i)
        print('next_url='+next_url)
        main(next_url)
