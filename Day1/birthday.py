#序列:字符串、列表、元组
# 根据年份判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'  #取余不是从鼠开始的，偷懒做法
#print(list(chinese_zodiac))
#print(chinese_zodiac[0])
#print(chinese_zodiac[0:4])
#print(chinese_zodiac[-1])
year = 2018
print(year%12)
print(chinese_zodiac[year%12])

print('狗' not in chinese_zodiac)

print(chinese_zodiac + 'abcd')

print(chinese_zodiac * 3)