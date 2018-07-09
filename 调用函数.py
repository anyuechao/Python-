#!/usr/bin/env python
#coding=utf-8
"""
    1.函数调用
    
    """

# 调用abs函数：(求绝对值)
abs(100)
abs(-20)
print("绝对值:{0},{1}".format(abs(100),abs(-20)))

#而max函数max()可以接收任意多个参数，并返回最大的那个：

max(1,2)
max(1,2,5,-1)

print("求最大值:{0},{1}".format(max(1,2),min(1,2,5,-1)))

#数据类型转换
a = float('123.02')
b = int('789')
c = bool('')
d = bool('1')
print("%d %d %s, %s" % (a,b,c,d))

a_abs = abs
print a_abs(100)











