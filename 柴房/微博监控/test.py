s="转发了 我的左脚 的微博:昨天下午我成功的混进了#西安·大明宫遗址[地点]#乐跑西安跑进新时代#  的现场，而且还混进大部队里完成了一项#吉尼斯#世界纪录# ，最后跟着大部队跑完全程，到达终点#西安·南院门[地点]# @朱荣2800com @抖音短视频  @何沛同志  @青之龙眼   勇往直前，青春昂扬 我的左脚的秒拍视频 ​​​  赞[6] 原文转发[1] 原文评论[1]转发理由:加油兄弟，认识了有快15年了吧。。。还没见过面，下次去西安！  赞[23] 转发[0] 评论[19] 收藏 今天 09:31 来自微博 weibo.com"


import re
# re.sub(pattern, repl, string, count=0, flags=0)

# pattern：表示正则表达式中的模式字符串；

# repl：被替换的字符串（既可以是字符串，也可以是函数）；

# string：要被处理的，要被替换的字符串；

# count：匹配的次数, 默认是全部替换
pattern=r'赞\[\d*\] 转发\[\d*\] 评论\[\d*\].*'
pattern=r赞\[\d*\] 转发\[1\]'
# pattern=r'赞\[23\] 转发\[0\] 评论\[19\].*'

repl=''
string=s
content=re.sub(pattern, repl, string)
print(content)


