# @Time    : 2018/10/31 16:00
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 耗时测试.py

from time import clock

start = clock()
L = [i for i in range(1, 10000000)]


num2, num5 = 0, 0
for num in L:
    while num % 2 == 0:
        num = num / 2
        num2 += 1
    while num % 5 == 0:
        num = num / 5
        num5 += 1

print(min(num2, num5))
end = clock()
print('time: {:.8f}s'.format(end - start))