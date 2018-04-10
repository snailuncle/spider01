from PIL import Image
import requests
import re

splitter = re.compile(r'\d{30}')  # 分割二值化后的图片


# distance('11110000', '00000000')
# 比较两个字符串有多少位不同, 返回不同的位数
def distance(string1, string2):
    d_str1 = len(string1)
    d_str2 = len(string2)
    d_arr = [[0] * d_str2 for i in range(d_str1)]
    for i in range(d_str1):
        for j in range(d_str2):
            if string1[i] == string2[j]:
                if i == 0 and j == 0:
                    d_arr[i][j] = 0
                elif i != 0 and j == 0:
                    d_arr[i][j] = d_arr[i - 1][j]
                elif i == 0 and j != 0:
                    d_arr[i][j] = d_arr[i][j - 1]
                else:
                    d_arr[i][j] = d_arr[i - 1][j - 1]
            else:
                if i == 0 and j == 0:
                    d_arr[i][j] = 1
                elif i != 0 and j == 0:
                    d_arr[i][j] = d_arr[i - 1][j] + 1
                elif i == 0 and j != 0:
                    d_arr[i][j] = d_arr[i][j - 1] + 1
                else:
                    d_arr[i][j] = min(d_arr[i][j - 1], d_arr[i - 1][j], d_arr[i - 1][j - 1]) + 1

    current = max(d_arr[d_str1 - 1][d_str2 - 1], abs(d_str2 - d_str1))
    return current


# 去除字符串里面连续的1
def no_one(string):
    n_arr = splitter.findall(string)
    n_arr = filter(lambda each_str: each_str != '111111111111111111111111111111', n_arr)
    n_result = ''
    for n_each in n_arr:
        n_result += str(n_each)

    return n_result


opener = requests.session()
res = opener.get('http://60.211.254.236:8402/Ajax/ValidCodeImg.ashx').content

with open('verify.gif', 'wb') as v:
    v.write(res)

img = Image.open('verify.gif')
img = img.convert('L')

size = img.size
# img = img.point(table, '1')
img_arr = img.load()

# img.save('after.gif')
inc = 0

str1 = ''
str2 = ''
str3 = ''
cur_str = ''
for x in range(size[0]):
    for y in range(size[1]):
        if img_arr[x, y] > 210:
            cur_str += '1'
        else:
            cur_str += '0'
        # print(img_arr[i, j], end='')
        # cur_str += str(img_arr[x, y])

    inc += 1
    if inc == 18:
        str1 = cur_str
        cur_str = ''
    elif inc == 36:
        str2 = cur_str
        cur_str = ''
    elif inc == 54:
        str3 = cur_str
        cur_str = ''

str1 = str1[:-60]
str2 = str2[:-60]
str3 = str3[:-60]
str1 = no_one(str1)
str2 = no_one(str2)
str3 = no_one(str3)
str1 = str1.strip('1')
str2 = str2.strip('1')
str3 = str3.strip('1')

with open('./dict/plus') as plus:
    with open('./dict/minus') as minus:
        p = plus.read()
        m = minus.read()
        is_add = 1 if distance(p, str2) < distance(m, str2) else 0

arr1 = []
arr3 = []

for each in range(1, 10):
    with open('./dict/{}'.format(each)) as f:
        ff = f.read()
        arr1.append([each, distance(ff, str1)])
        arr3.append([each, distance(ff, str3)])

arr1 = sorted(arr1, key=lambda item: item[1])
arr3 = sorted(arr3, key=lambda item: item[1])
result = arr1[0][0] + arr3[0][0] if is_add else arr1[0][0] - arr3[0][0]
print(result)
