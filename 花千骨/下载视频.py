#目标:下载花千骨全集
import requests,re,time

# copy /b  D:\spider01\花千骨\*.ts  D:\spider01\花千骨\new.ts

S = requests.Session()

def video_get_from_url(target_url,serial_numbers):
    target_response = S.get(url=target_url, stream=True)
    target_html = target_response.content
    # http://dx.data.video.qiyi.com/videos/v0/20150610/10/7e/ef4a46e037b0eff76a521644399d7117.ts?
    file_name=re.search(r'(\w+?(?=\.ts\?))', target_url).group()
    # with open(r'D:/spider01/花千骨/'+str(file_name)+'.ts','ab') as f:
    with open(r'D:/spider01/花千骨/'+'花千骨第一集'+'.ts','ab') as f:
        f.write(target_html)

#读取文本,提取url
#D:\spider01\爱奇艺\花千骨.txt
txt_path=r"D:\spider01\爱奇艺\花千骨.txt"
pattern =re.compile('http://.*?(?= )')
with open(txt_path,'r') as f:
    content=f.read()
# print(content)
result= pattern.finditer(content)
serial_numbers=1
for match in result:
    url=match.group().strip()
    print(serial_numbers)
    try:
        video_get_from_url(url,serial_numbers)
        serial_numbers+=1
        time.sleep(0.003)
    except Exception as e:
        print(e)
# with open(str(serial_numbers),'ab') as f:
#     f.write(target_html)






