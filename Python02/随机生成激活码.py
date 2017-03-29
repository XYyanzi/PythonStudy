# coding: utf-8

import random

'''
随机生成500个激活码，格式如下：XXXX-XXXX-XXXX-XXXX，每一位是数字或者大写英文字母。
'''
# 生成一个97到122之间的序列
# 97-122 对应从“a”到“z”的ASCII码
# 收集 A-Z
def genCode():
    letter = []
    for i in range(97, 123):
        letter.append(chr(i).upper())
    # print letter

    # 收集 0-9
    num = []
    for i in range(10):
        num.append(i)
    # print num
    #  将字母和数字放到一个list里面
    ran = num + letter
    # print ran

    list = []
    for i in range(4):
        group = ''
        for j in range(4):
            # 随机选择一个元素
            # code = random.choice(ran)
            code = ran[random.randint(0, len(ran)-1)]
            group += str(code)
        list.append(group)
        # print list

    result = '-'.join(list)
    print('随机生成的激活码是：'+ result )

for j in range(10):
    genCode()
