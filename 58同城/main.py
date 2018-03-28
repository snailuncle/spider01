from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)

def main():
    pool=Pool()
    pool.map(get_all_links_from,channel_list.split())

if __name__ == '__main__':
    main()






















