from multiprocessing import Pool
import time


def son_process(name):
    time.sleep(5)
    print "Process %s is running\n" % name


pool = Pool(4)
print "Son process is started"
for x in range(0, 10):
    pool.apply_async(son_process, args=('son_%d'%x,))
pool.close()
print "Mark"
pool.join()

print "Son process is ended - Printed by Main Process"
