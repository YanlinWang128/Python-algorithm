# @Time    : 2018/10/31 15:57
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 末尾0的个数.py

from time import clock

start = clock()

L, num5 = [i for i in range(1, 10000000)], 0

for num in L:
    while num % 5 == 0:
        num = num / 5
        num5 += 1
print(num5)

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
题目: 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。
(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。


我们在计算n的阶乘时，实际上就是把所有小于等于n的正整数分解成质因数，然后再将其乘到一起
末尾0的个数实际上就是2*5的个数
因2的个数明显是很多很多的，所以问题就转化成了5的个数

即就每个数可以由几个5相乘，再把全部的5加到一起就是了。

num2, num5 = 0, 0
for num in L:
    while num % 2 == 0:
        num = num / 2
        num2 += 1
    while num % 5 == 0:
        num = num / 5
        num5 += 1

print(min(num2, num5))
"""
