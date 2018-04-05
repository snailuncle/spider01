import os
DIR = r'D:/spider01/花千骨/' 
def filetime(file):
    stat_file = os.stat(DIR + "/" + file)
    last_access_time = stat_file.st_ctime
    return last_access_time
def sort_file(dir_name):
    iterms = os.listdir(dir_name)
    iterms = sorted(iterms,key= lambda x:filetime(x),reverse=False)
    return iterms

sort_file(DIR)


