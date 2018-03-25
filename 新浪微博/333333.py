import configparser

config_path='keyword.ini'
section_name='section_one'
keyword='a'

# #写入ini
# with open(config_path,'w+') as f:
#     cfg = configparser.ConfigParser() 
#     cfg.add_section(section_name) 
#     cfg.set(section_name,'abc','123') 
#     cfg.write(f) 


with open(config_path,'r+') as f:
    cfg = configparser.ConfigParser() 
    section_list=cfg.sections() 
    print(section_list)


cfg=configparser.ConfigParser()

cfg.read(config_path)

section_list=cfg.sections()

print(section_list)
