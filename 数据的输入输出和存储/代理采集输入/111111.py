


import os,time,sys
proxy_txt=r"D:\Documents\Tencent Files\1789500304\FileRecv\proxy.txt"

with open(proxy_txt,'r') as f:
    content=f.read()
# print(content)

content_list=content.split('\n')
# print(content_list)
# print(type(content_list))
# print(len(content_list))
proxy_list=[]
for i in content_list:
    if i:
        info=i.split(':')
        # print(info)
        proxy_dict='{{"port":"{0}","ip":"{1}"}}'.format(info[1],info[0])
        proxy_list.append(eval(proxy_dict))
        
# json_proxies1={"code":"0","msg":[{"port":"49593","ip":"123.55.69.70"},{"port":"31835","ip":"115.48.85.231"}]}
json_proxies1={"code":"0","msg":[]}
json_proxies1['msg']=proxy_list
print(json_proxies1)

    # sys.exit()
