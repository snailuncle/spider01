from subprocess import * 
import subprocess
import subprocess as sp   
file_out = subprocess.Popen('ping www.baidu.com', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while True:
    line = file_out.stdout.readline()
    print(line)
    if subprocess.Popen.poll(file_out)==0: #判断子进程是否结束
        break
