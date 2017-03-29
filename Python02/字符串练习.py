# coding: utf-8

# 获取字符串长度
print (len('python'))

# 连接字符串，可以直接使用+连接
print ('abc' + 'def')
s = 'python'
s += '\n'
s += 'study'
# 格式化 %
print ('%s' % 'python')
print ('%s' % s)
print ('%s, %d, %f' % ('python', 100, 10.23))
print ('%s, %d, %2f' % ('python', 100, 10.23987))

# 两个字符串的比较
print ('abs' > 'dfe')

# 字符串位置
s1 = 'python lesson'
s2 = 'ho'
s3 = 'leson'

print (s1.index(s2))

# 去掉开头和结尾的空格
s = '    python study  '
print s
print (s.strip())   # 去掉字符串开头和结尾的空格
print (s.lstrip())  # 去掉字符串开头的空格
print (s.rstrip())  # 去掉字符串结尾的空格

# 字母大小写转换
s = 'python'
print (s.upper())   # 全部字母转换成大写
print (s.upper().lower())  # 全部字母转换成小写
print (s.capitalize())     # 首字母转换成大写


# 切分与拼接
s = 'abd,bcd*efs'
ss = s.split(',')     # 用','来切分字符串，前置条件是必须含有','这个字符
print ss

b = '121312*121312*1211'
bb = b.split('*')
print bb

ss = ['1233', '31212', 'sdfsdf']
jj = '##'.join(ss)
print jj

# 判断
s = 'abcdefg'
print(s.startswith('abs'))
print(s.startswith('abc'))   # 判断是否以abc开头
print s.endswith('efg')      # 判断是否以efg结尾
print 'abcd1234'.isalnum()   # 判断abcd1234是否以字母或数字开头
print '\tabcd1234'.isalnum()  # 判断\tabcd1234 是否以字母或数字开头
print('abcd'.isalpha())    # 判断字符串是否只由字母组成
print '12133'.isdigit()    # 判断字符串是否只由数字组成
print('  '.isspace())     # 判断字符串是否是空格
print('acb125'.islower())    # 判断字符串中的字母是否全是小写字母
print('A1B2C'.isupper())     # 判断字符串中的字母是否全是大写字母
print('Hello world!'.istitle())   # 判断字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。



# dir函数——查看参数类型支持的所有函数或方法

print(dir(int))
print(dir('abc'))

class MyClass:
    def func():
        print('MyClass:func')
print(dir(MyClass))


# type函数——返回参数的类型
print(type('abcdd'))
print(type(1234))
print(type([1, 2, 3]))
print(type((1234, 212)))
