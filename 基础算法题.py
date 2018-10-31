# @Time    : 2018/10/31 11:01
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 基础算法题.py

from  math import sqrt


# 1. 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）

print(' '.join([str(i) for i in range(2, 100) if 0 not in [i % j for j in range(2, int(sqrt(i)) + 1)]]))
"""
# 使用join 实现间隔问题最强, 可满足最后一个数字没有空格,  注意range 左闭右开
# 素数问题: 记住最小的素数是 2
"""
