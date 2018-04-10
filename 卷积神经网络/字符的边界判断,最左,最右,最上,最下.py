from Queue import Queue
def cfs(im,x_fd,y_fd):
    '''用队列和集合记录遍历过的像素坐标代替单纯递归以解决cfs访问过深问题
    '''

    # print('**********')

    xaxis=[]
    yaxis=[]
    visited =set()
    q = Queue()
    q.put((x_fd, y_fd))#列表存放坐标
    visited.add((x_fd, y_fd))#set存放坐标
    offsets=[(1, 0), (0, 1), (-1, 0), (0, -1)]#四邻域  右上左下
    #记录给定点连接的所有黑色点
    while not q.empty():
        x,y=q.get()

        for xoffset,yoffset in offsets:
            #neighbor邻居
            x_neighbor,y_neighbor = x+xoffset,y+yoffset

            if (x_neighbor,y_neighbor) in (visited):
                    continue    # 已经访问过了

            visited.add((x_neighbor, y_neighbor))

            try:
                if im[x_neighbor, y_neighbor] == 0:#0表示黑色
                        xaxis.append(x_neighbor)
                        yaxis.append(y_neighbor)
                        q.put((x_neighbor,y_neighbor))

            except IndexError:
                pass
    # print(xaxis)
    # | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
    #相当于or
    if (len(xaxis) == 0 | len(yaxis) == 0):
        xmax = x_fd + 1
        xmin = x_fd
        ymax = y_fd + 1
        ymin = y_fd

    else:
        xmax = max(xaxis)
        xmin = min(xaxis)
        ymax = max(yaxis)
        ymin = min(yaxis)
        #ymin,ymax=sort(yaxis)
    #返回所有连接的   黑色点的最值,
    #也就是确定一个字符的显示区域, 长方形
    return ymax,ymin,xmax,xmin
#detect侦查
def detectFgPix(im,xmax):
    '''搜索区块起点
    '''
    #shape返回一个元组
    # 第一个元组表示图像数组的大小（行、列、颜色通道）
    #返回最右边的黑点
    h,w = im.shape[:2]
    for y_fd in range(xmax+1,w):
            for x_fd in range(h):
                    if im[x_fd,y_fd] == 0:
                            return x_fd,y_fd

def CFS(im):
    '''切割字符位置
    '''

    zoneL=[]#各区块长度L列表
    zoneWB=[]#各区块的X轴[起始，终点]列表
    zoneHB=[]#各区块的Y轴[起始，终点]列表

    xmax=0#上一区块结束黑点横坐标,这里是初始化
    for i in range(10):

        try:
                #最右边的黑点
                x_fd,y_fd = detectFgPix(im,xmax)
                # print(y_fd,x_fd)
                # 包含最右边黑点的  黑点相连的区域
                xmax,xmin,ymax,ymin=cfs(im,x_fd,y_fd)
                L = xmax - xmin
                H = ymax - ymin
                zoneL.append(L)
                zoneWB.append([xmin,xmax])
                zoneHB.append([ymin,ymax])

        except TypeError:
                return zoneL,zoneWB,zoneHB

    return zoneL,zoneWB,zoneHB
