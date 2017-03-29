# coding: utf-8

'''
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。 如果不存在，则返回 -1。
'''

source = 'In all time before now and in all time to come, there has never been and will never be anyone just like you.' \
         'You are unique in the entire history and future of the universe. Wow! Stop and think about that!' \

target = 'future'

# 一种使用捕获异常的方法
# try:
#     find = source.index(target)
#     print find
# except Exception:
#     print -1

# 一种使用条件判断的方法
if target in source:
    find = source.index(target)
    print find
else:
    print -1

def strstr(source, target):
    if (source is None) or (target is None):
        return -1
    for i in range(len(source) - len(target) + 1):
        if source[i:i + len(target)] == target:
            return i
    return -1

print strstr(source, target)
