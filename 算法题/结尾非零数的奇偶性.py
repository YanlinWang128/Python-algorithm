# @Time    : 2018/10/31 16:14
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 结尾非零数的奇偶性.py

from time import clock
from functools import reduce

start = clock()

# L = [i for i in range(1, 232442)]
L = [1, 3, 5, 4]


def cal(x, y):
    result = x * y
    while result % 10 is 0:
        result /= 10
    return int(str(result)[-1:])


print(0 if reduce(cal, L) % 2 is 0 else 1)

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。
如果为奇数输出1,偶数则输出0


每次取 最后一位非零数
"""
