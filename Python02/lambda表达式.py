# coding: utf-8

# 函数也是普通对象

def add(x, y):
    return x + y

f = add
print(f(100, 200))
print('')

# 函数可以作为参数被传递
def g(f, x, y):
    print(f(x, y))

g(f, 100, 200)
print('')

# 匿名函数
g(lambda x, y: x + y, 300, 500)
print('')

# map操作
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(lambda x: x * x, numbers)
print(list(squares))
print('')

# reduce操作
from functools import reduce
print(reduce(add, numbers))
print(reduce(lambda x, y: x + y, numbers))

# 阶乘
from functools import reduce
l = [1, 2, 3, 4, 5]        # 求5的阶乘  1*2*3*4*5
print (reduce(lambda x, y: x * y, l))
print (reduce(lambda x, y: x * y, range(1, 6), 2)) # 求5的阶乘 再*2 1*2*3*4*5*2

