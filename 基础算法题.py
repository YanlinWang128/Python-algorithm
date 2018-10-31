# @Time    : 2018/10/31 11:01
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 基础算法题.py

from  math import sqrt
from time import clock

# 1.素数问题
# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）

print(' '.join([str(i) for i in range(2, 100) if 0 not in [i % j for j in range(2, int(sqrt(i)) + 1)]]))
"""
# 使用join 实现间隔问题最强, 可满足最后一个数字没有空格,  注意range 左闭右开
# 素数问题: 记住最小的素数是 2
"""

# 2. 中位数
# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）
# 例如： L=[0,1,2,3,4] 则输出：2

L = [i for i in range(169)]
length = len(L)
L.sort()
if length % 2 != 0:
    print(L[int(length / 2)])
else:
    print((L[int(length / 2)] + L[int(length / 2) - 1]) / 2.00)
# 三元表达式
print(L[int(length / 2)] if length % 2 else (L[int(length / 2)] + L[int(length / 2) - 1]) / 2.0)
"""
求中位数:1. 判断列表长度  2. 对列表进行排序
"""

# 3. 最大公约数
# 给你两个正整数a和b， 输出它们的最大公约数
# 例如：a = 3, b = 5 则输出：1

a, b = 3, 9
print(max([i for i in range(1, a + 1 if a < b else b + 1) if a % i == 0 and b % i == 0]))
"""
1. 判别a, b 大小, 三元表达式
"""
# 4. 最小公倍数
# 给你两个正整数a和b， 输出它们的最小公倍数。
# 例如：a = 3, b = 5 则输出：15

a, b = 3, 5
print(a * b / max([i for i in range(1, a + 1 if a < b else b + 1) if a % i == 0 and b % i == 0]))
"""
1. 最小公倍数是 两数乘积的最大公约数

"""

# 结尾0的个数
# 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
# 例如： L=[2,8,3,50], 则输出：2
start = clock()
L = [i for i in range(50)]

num2 = 0
num5 = 0
for num in L:
    while num % 2 == 0:
        num = num / 2
        num2 += 1
    while num % 5 == 0:
        num = num / 5
        num5 += 1

print(min(num2, num5))
end = clock()
print('耗时: {:.8f}'.format(end - start))
