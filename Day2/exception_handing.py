#i=j
#print())
#a='123'
#print(a[3])
#
# d = {'a':1,'b':2}
# print(d[c:])

#year = int(input('请用户输入出生年份：'))

# try:
#     year = int(input('请用户输入出生年份：'))
# except ValueError:
#     print('年份要输入数字')
# a=123
# a.append()

#except {ValueError,AttributeError,KeyError}
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能作除数 %s ' %e)

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()