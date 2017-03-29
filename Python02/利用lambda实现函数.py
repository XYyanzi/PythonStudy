# coding: utf-8

'''
实现函数fn(n)，返回一个函数f，f(x) = n * x。（利用lambda表达式）
'''

def fn(n):
    f = lambda x: n * x
    return f

f= fn(5)  # 实际上 f = f(x)=5*x   f 是一个函数，参数是x
result = f(100)   # 实际上 f(100) = 5 * 100
print result
