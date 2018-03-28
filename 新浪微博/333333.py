
import configparser

config_path = 'keyword.ini'
section_name = 'section_one'

with open(config_path,'w+') as f:
    cfg = configparser.ConfigParser() 
    cfg.readfp(f)
    # cfg[section_name] = {'ccc':'ddd'}
    cfg[section_name] = {}
    cfg.set(section_name,'aaa','bbb')
    cfg.write(f)
