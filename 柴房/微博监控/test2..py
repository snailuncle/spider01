import json,os
a = {'name': 'wang',"老王":"帽子"}
content={}
if  os.path.exists('weibonick.txt'):
    print(os.path.getsize('weibonick.txt'))
    if os.path.getsize('weibonick.txt')<6:
        pass
    else:
        with open('weibonick.txt', 'r+') as f:
            content=json.load(f)

        print(content)
        print(type(content))
        print(content['杨幂'])
content['杨幂']='666'
with open('weibonick.txt', 'w') as f:
    json.dump(content,f)

with open('weibonick.txt', 'r') as f:
    content=json.load(f)

print(content)
print(type(content))
