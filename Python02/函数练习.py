# coding: utf-8

def add(x, y = 100, z = 200):
    return x + y + z

# 普通调用
print(add(100, 200, 300))

# 默认参数
print(add(600))
print(add(100, 200))

# 带名字的参数
print(add(z=300, x=100, y=200))
print(add(x=500))
print('')

# 可变参数：*
def mySum(*numbers):  # numbers是数组
    s = 0
    for i in numbers:
        s += i
    return s
print(mySum(1, 2, 3, 4))

# 可变参数：**
def printUser(name, age, **kv): # kv是字典
    print('name: %s' % name)
    print('age: %s' % age)
    print(kv)
printUser('Tom', 18, gender='male', city='NY')
