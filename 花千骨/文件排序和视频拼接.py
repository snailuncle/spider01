from natsort import natsorted
# 主要是需要moviepy这个库

import os,sys

def filetime(file):
    DIR=r'D:/spider01/花千骨/'
    print(DIR+file)
    stat_file = os.stat(DIR+file)
    last_access_time = stat_file.st_ctime
    return last_access_time
def sort_file(list_file):
    iterms = sorted(list_file,key= lambda x:filetime(x),reverse=False)
    return iterms



# 访问 video 文件夹 (假设视频都放在这里面)

# os.listdir(path)
# os.utime(path, times)
# 按文件名排序
# files.sort()
path=r'D:/spider01/花千骨/'
files=os.listdir(path)
files = sort_file(files)
# 遍历所有文件
file_path=''
for file in files:
    print(file)
    # 如果后缀名为 .ts
# ffmpeg -i "concat:input1.mpg|input2.mpg|input3.mpg" -c copy output.mpg
    
    if os.path.splitext(file)[1] == '.ts':
        # # 拼接成完整路径
        # filePath = os.path.join(root, file)
        # # 载入视频
        # video = VideoFileClip(filePath)
        # # 添加到数组
        # L.append(video)
        file_path=file_path+file+'|'
file_path=file_path[0:-1]
print(file_path)            
str_video='ffmpeg -i \"concat:'+file_path+'\" -c copy output.ts'
print(str_video)
# sys.exit()
os.popen(str_video)
# ffmpeg -i "concat:input1.mpg|input2.mpg|input3.mpg" -c copy output.mpg

