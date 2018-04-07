# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

# target 是函数名字，需要调用的函数
# args 函数需要的参数，以 tuple 的形式传入
# name = multiprocessing.current_process().name

import multiprocessing
import os,time

def run_proc(name):
    print('Child process {0} {1} Running '.format(name, os.getpid()))
    time.sleep(2)

if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()
    p.join()
    print('Process close')



# Pool 可以提供指定数量的进程供用户使用，默认是 CPU 核数。当有新的请求提交到 Poll 的时候，如果池子没有满，会创建一个进程来执行，否则就会让该请求等待。 
# - Pool 对象调用 join 方法会等待所有的子进程执行完毕 
# - 调用 join 方法之前，必须调用 close 
# - 调用 close 之后就不能继续添加新的 Process 了



















