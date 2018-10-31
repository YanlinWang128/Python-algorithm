# @Time    : 2018/10/31 17:45
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 二进制下1的个数.py

from time import clock


start = clock()
a = 9

if a < 0:
    a = a & 0xffffffff  # 获得负数的补码

count = 0
while a:
    count += 1
    a = (a - 1) & a

print(count)

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
给你一个整数a，数出a在二进制表示下1的个数，并输出

二进制整数处理算法: 将它减一和它本身相与，会把这个整数最右边的1变为零

负数我们在计算时使用了他的补码进行计算，将最高位的符号位取反就可以获得补码
通常我们采用和0xFFFFFFFF相与来得到。这样得到了一个32位的二进制数据。

负数用补码表示
"""