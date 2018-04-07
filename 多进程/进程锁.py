lock = multiprocessing.Lock()
lock.acquire()
lock.release()
with lock:
