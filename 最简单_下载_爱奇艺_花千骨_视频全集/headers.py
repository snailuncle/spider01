headers='''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Host: www.iqiyi.com
Referer: http://www.iqiyi.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36
'''
import re
def headers_format(headers):
    # sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
    new_headers=re.sub(r'(.*): (.*)',r'"\1":"\2",',headers)
    new_headers=new_headers.strip()[0:-1]
    print(new_headers)
    return new_headers

headers_format(headers)
















# sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
# 当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
# 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
# count用于指定最多替换次数，不指定时全部替换。 

# import re
 
# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
 
# print p.sub(r'\2 \1', s)
 
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
 
# print p.sub(func, s)
 
# ### output ###
# # say i, world hello!
# # I Say, Hello World!
