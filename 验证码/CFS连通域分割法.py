import queue

def cfs(img):
    """传入二值化后的图片进行连通域分割"""
    pixdata = img.load()
    w,h = img.size
    visited = set()
    q = queue.Queue()
    offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    cuts = []
    for x in range(w):
        for y in range(h):
            x_axis = []
            #y_axis = []
            if pixdata[x,y] == 0 and (x,y) not in visited:
                q.put((x,y))
                visited.add((x,y))
            while not q.empty():
                x_p,y_p = q.get()
                for x_offset,y_offset in offset:
                    x_c,y_c = x_p+x_offset,y_p+y_offset
                    if (x_c,y_c) in visited:
                        continue
                    visited.add((x_c,y_c))
                    try:
                        if pixdata[x_c,y_c] == 0:
                            q.put((x_c,y_c))
                            x_axis.append(x_c)
                            #y_axis.append(y_c)
                    except:
                        pass
            if x_axis:
                min_x,max_x = min(x_axis),max(x_axis)
                if max_x - min_x >  3:
                    # 宽度小于3的认为是噪点，根据需要修改
                    cuts.append((min_x,max_x))
    return cuts
