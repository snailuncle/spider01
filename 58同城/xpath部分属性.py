# f、部分属性值匹配
# WebElement ele = driver.findElement(By.xpath("//input[start-with(@id,'fuck')]"));//匹配id以fuck开头的元素，id='fuckyou'
# WebElement ele = driver.findElement(By.xpath("//input[ends-with(@id,'fuck')]"));//匹配id以fuck结尾的元素，id='youfuck'
# WebElement ele = driver.findElement(By.xpath("//input[contains(@id,'fuck')]"));//匹配id中含有fuck的元素，id='youfuckyou'
# g、使用任意值来匹配属性及元素
# WebElement ele = driver.findElement(By.xpath("//input[@*='fuck']"));//匹配所有input元素中含有属性的值为fuck的元素



# from lxml import etree
# div = etree.HTML(html)
# table = div.xpath('//div/table')[0]
# content = etree.tostring(table,print_pretty=True, method='html')  # 转为字符串
#     html=etree.tostring(link,encoding='unicode',pretty_print=True,method='html')



# info = data.xpath('string(.)').extract()[0]  
