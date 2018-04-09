import os  
  
#创建目录  
os.mkdir("D:\\python\\2")  
#删除目录  
os.rmdir("D:\\python\\2")  
  
#创建多级目录  
os.makedirs("D:\\python\\oo\\2\\3")  
#删除多级目录  
os.removedirs("D:\\python\\oo\\2\\3");  
  
#获取目录下文件夹及文件  
paths=os.listdir("D:\\python")  
for path in paths:  
    print(path)  
      
#获取当前目录位置  
path1=os.getcwd()  
print(path1)  
  
#切换目录  
os.chdir("D:\\python\\oo\\3")  
path2=os.getcwd()  
print(path2)  
  
#遍历所有子目录及文件  
for p1,d,filelist in os.walk('D:'+os.sep+'python'):  
    for f1 in filelist:  
        fp=os.path.join(p1,f1)  
        print(fp)  

# os.walk(）返回Directory tree generator。每次生成格式为（dirpath, dirnames, filenames） 的tuple，元素依次是当前路径、当前路径下文件夹列表、当前路径下文件名列表。
