# file1 = open('name.txt','w')
# file1.write('1.诸葛亮')
# file1.close()

# file2 = open('name.txt')
# print(file2.read())
# file2.close()

# file3=open('name.txt','a')
# file3.write('刘备')  #尾部追加，不分行
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())
# file4.close()

# file5 = open('name.txt')
# for line in(file5.readlines()):
#     print(line)
#     print('####')
# file5.close()

file6 = open('name.txt')
print('当前文件指针位置 %s' %file6.tell())
print('当前读到了一个字符，字符的内容为%s' %file6.read(1))
print('当前文件指针位置 %s' %file6.tell())
# 第一个参数代表偏移位置，第二个参数 0 表示从文件开头偏移  1 表示从当前位置偏移   2 从文件结尾偏移
file6.seek(5,0)  #汉字占两个位置
print('我们进行了seek操作')
print('当前文件指针位置 %s' %file6.tell())
print('当前读到了一个字符，字符的内容为%s' %file6.read(1))
print('当前文件指针位置 %s' %file6.tell())
file6.close()