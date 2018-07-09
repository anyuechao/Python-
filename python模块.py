#!/usr/bin/env python
#coding=utf-8

# classmates =['Michael' , 'Bob', 'Tracy']
# for i in classmates:
#     print ("%s是咱们班的学生" % i)
#     print ("{0}是咱们班的学生".format(i))

# print("咱班一共有%s人" % len(classmates))

# '''1.1 查
#     访问list中每一个元素的位置
#     访问list中每一个位置的元素
    
#     list 越界
#     File "<stdin>", line 1, in <module>
#     IndexError: list index out of range
#     '''

# print("第一位同学{0}".format(classmates[0]))
# print("第一位同学{0},第二位同学{1}".format(classmates[0]).format(classmates[0]))
# print("最后一个同学为%s" % classmates[len(classmates) - 1])
# print("最后一个同学为%s" % classmates[ - 1])
# print("倒数第二个同学为%s" % classmates[ - 2])

'2222222222222222'

# def func1():
# 	print('sss');

# def func2():
# 	pass

# func1();
# func2

# import math

# def func3(x,y,z):
# 	if (x > y and z != 0):
# 	    return math.cos(x) + math.sin(y) - z
# 	else:
# 	    return x
	


# c = func3(1,45,6);

# print c;

'3333333333333333'
 
# a = list(range(1,100))
# # print a

# def func4(list = []):
# 	l = list[:]
# 	for x in list:
# 		l.append(x * x)
# 		print x
# 	return l	

 
# g = func4(a)
# print g;


'444444444444444444'


# L = [x * x for x in xrange(10)]

# print L

# G = (x * x for x in xrange(10))
# print G

# for x in xrange(0,10):
# 	print next(G)



'555555555555555555'

# '''
# 斐波切纳周期函数
# 	'''
# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		print(b)
# 		a,b = b,a + b
# 		n = n + 1
# 	return 'down'
	

# fib(20)

'555555555555555555'
# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		yield b
# 		a , b = b , a + b
# 		n = n + 1
# 	return 'done'

# g = fib(10)
# print g
# for x in xrange(10):
#  	next(g)
#  	print 
'666666666666666666'
# '''
# 错误捕获
# '''
# def odd():
# 	print('step 1')	
# 	yield 1
# 	print('step 2')	
# 	yield 2
# 	print('step 3')	
# 	yield(5)
# o = odd()
# for x in xrange(10):
# 	try:
# 		x = next(o)
# 		print ('x:' ,x)
# 	except StopIteration as e:
# 		print('Generator return value:',e.value)
# 		break


'7777777777777777777'
# def clac_Sum(*args):
# 	ax = 0
# 	for n in args:
# 		ax = ax + n
# 	return ax

# def lazy_Sum(*args):
# 	def sum():
# 		ax = 0
# 		for n in args:
# 			ax = ax + n
# 		return ax
# 	return sum


# f1 = lazy_Sum(1,2,3,45,6)
# f2 = lazy_Sum(1,2,3,45,6)

# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f():
# 			return i * i
# 		fs.append(f)
# 	return fs

# f1 = count()


'888888888888888888888'

'''
	装饰器
	'''
# 匿名函数
# '''
# f = lambda x: x *x 

# def build(x,y):
# 	return lambda: x * x + y * y

# c = build (2,5) 

# '''拿到函数的名字'''
# def now():
# 	print 1231231

# f = now

# print f.__name__

# '''
# 打印函数名称
# 	'''
# def log(func):
# 	def wrapper(*args,**kw):
# 		print('call %s():'% func.__name__)
# 		return func(*args,**kw)
# 	return wrapper
# # @log

# def now():
# 	print('2015-3-25')

# # now() 

# now =  log(now)

# now()

# print int('1011110',base = 8)

# print int('1011110',base = 16)

# def int2(x,base = 2):
# 	return int(x,base)

# print int2('100000')

# import functools
# int2 = functools.partial(int,base = 2)
# print int2('100000')



'===================模块======================'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Yuechao An'

# import sys
# def test():
# 	args = sys.argv
# 	if(len(args) == 1):
# 		print 'hello'
# 	elif len(args) == 2:
# 		print ('hello，%s',args[1])
# 	else:
# 		print('too many arguments')

# if __name__ == '__main__':
# 	test()


# print sys.argv


'''
正则表达式
	'''
import re

# c = re.match(r'^\d{3}\-\d{3,8}$','010-12345')

# if c :
# 	print 'YES'
# else:
# 	print 'NO'




a = re.split(r'[\s\,\;\{\}\;]+','a,;;;,as,s,s,s,,as,a,fwe,f,w,ef;as;da,sd;  a,sd;as ,asd ;asd;;;;,,;,l;,l{sasas,as;')

print a



























