# file1 = open('name.txt','w')
# file1.write('诸葛亮')
# file1.close()
#
# file3=open('name.txt','a')
# file3.write('刘备')
# file3.close()
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file4 = open('name.txt')
# print(file4.readline())
# file4.close()
#
# file5 = open('name.txt')
# for line in(file5.readlines()):
#     print(line)
#     print('####')
# file5.close()

file6 = open('../venv/name.txt')
print('当前文件指针位置 %s' %file6.tell())
print('当前读到了一个字符，字符的内容为%s' %file6.read(1))
print('当前文件指针位置 %s' %file6.tell())
file6.seek(0)
print('我们进行了seek操作')
print('当前文件指针位置 %s' %file6.tell())
print('当前读到了一个字符，字符的内容为%s' %file6.read(1))
print('当前文件指针位置 %s' %file6.tell())
file6.close()