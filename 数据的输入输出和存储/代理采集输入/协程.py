import  asyncio
import threading
# 异步IO例子：适配Python3.5，使用async和await关键字
async def hello(index):       # 通过关键字async定义协程
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread()))
    await asyncio.sleep(1)     # 模拟IO任务
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread()))

loop = asyncio.get_event_loop()     # 得到一个事件循环模型
tasks = [hello(1), hello(2)]        # 初始化任务列表
loop.run_until_complete(asyncio.wait(tasks))    # 执行任务
loop.close()   
# async关键字将一个函数声明为协程函数，函数执行时返回一个协程对象。

# await关键字将暂停协程函数的执行，等待异步IO返回结果。
