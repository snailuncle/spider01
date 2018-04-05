f=open(r'D:\spider01\编码网页\output.html', 'r',encoding='utf-8')
content=f.read()
f.close()
# #encode    str  -> bytes
#这两种编码都可以
# content=content.encode('utf_8_sig')
content=content.encode('raw_unicode_escape')
print(type(content))
print(content)
print('\n\n\n')

# #decode   bytes -> str
content=content.decode('unicode-escape')
print(type(content))
print(content)
print('\n\n\n')

# ---------------------
content=content.encode('raw_unicode_escape')
print(type(content))
print(content)
print('\n\n\n')

# #decode   bytes -> str
content=content.decode('utf-8')
print(type(content))
print(content)
print('\n\n\n')




