# coding: utf-8

# 如何实现传统的 for (i = 0; i < n; i += step)
for i in range(0, 10, 3):  # [0, 10)，步长为3
    print(i)

# 步长可以是负数  等价 for (i = 3; i > -1; i -= 2)
for i in range(5, -2, -2):   # [5，-2）, 步长为-2
    print(i)


# while循环
s, i = 0, 1
while i < 101:     # 当while语句后面的条件为true时，执行下面的语句
    s += i         # s = s + i
    i += 1         # i = i+1
print(s)


# break和pass
for i in range(5):
    print i
    if i < 2:
        pass
    elif i < 4:
        print(i)
    else:
        break


cond = True
if cond:
    print(True)
else:
    print(False)
cond = False
if not cond:
    print(False)
cond = None   # 与False等价
if not cond:
    print(None)
# 空的容器与False等价
li = []  # 尝试改成[1, 2, 3, 4]
if li:
    print('Not empty')
else:
    print('Empty')

list = [1, 2, 3, 4]

if list:
    print ('Not empty')
else:
    print('Empty')

