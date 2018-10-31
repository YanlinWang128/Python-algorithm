# @Time    : 2018/10/31 18:27
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 字符串大小写转换.py

from time import clock

start = clock()

a = 'hello, world'
print(a.lower())

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
 str.upper(),lower(),title(), 返回一个字符串
"""