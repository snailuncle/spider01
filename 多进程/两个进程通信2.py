from multiprocessing import Process, Pipe

def talk(pipe):
    pipe.send(dict(name='Bob', spam=42))            # 传输一个字典
    reply = pipe.recv()                             # 接收传输的数据
    print('talker got:', reply)

if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()                  # 创建两个 Pipe() 实例，也可以改成 conf1， conf2
    child = Process(target=talk, args=(childEnd,))  # 创建一个 Process 进程，名称为 child
    child.start()                                   # 启动进程
    print('parent got:', parentEnd.recv())          # parentEnd 是一个 Pip() 管道，可以接收 child Process 进程传输的数据
    parentEnd.send({x * 2 for x in 'spam'})         # parentEnd 是一个 Pip() 管道，可以使用 send 方法来传输数据
    child.join()                                    # 传输的数据被 talk 函数内的 pip 管道接收，并赋值给 reply
    print('parent exit')
