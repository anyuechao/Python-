#!/usr/bin/env python
#coding=utf-8

"""1.条件判断和循环
    计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
    比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
    
    """
age = 12
if age >= 18:
    print 'your age is %s is a Adult' % age
else:
    print ("your age is {0} is a student".format(age))


age = 12
if age >= 18:
    print 'your age is %s is a Adult' % age
elif age == 18:
    print 'your age is %s' % age
else:
    print ("your age is {0} is a student".format(age))


'''
    if判断条件还可以简写，比如写：
    只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
    '''
x = 0;

if x:
    print 'True'

"""2.循环 for...in
    Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
    """

names = ['Michael','Bob','Tracy']
for name in names:
    print name


#累加

sum = 0
for x in (1,2,3,4,5,6,7,8,9,10):
    sum = sum + x
print sum

'''2.1 range()
    Python提供一个range()函数，可以生成一个整数序列，比如range(5)生成的序列是从0开始小于5的整数：
    '''

sum_1 = 0
for x in range(101):
    sum_1 = sum_1 + x
print '从1-100的合为{0}'.format(sum_1)


"""3.while
    第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
    """
#在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
sum_2 = 0
n = 99
while n > 0:
    sum_2 = sum_2 + n
    n = n - 2
print "sum_2{0}".format(sum_2)



"""3.再议输出raw_input

    """
birth = raw_input('birth:')
if birth < 2000:
    print '00前'
else:
    print '00后'

#输出错误的原因:原来从raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型：
birth_1 = int(raw_input('birth:'))
if birth_1 < 2000:
    print '00前'
else:
    print '00后'


"""
    如果把非数字的字符串转化为int()则报错
    原来int()发现一个字符串并不是合法的数字时就会报错，程序就退出了。
    """

""""循环是让计算机做重复任务的有效的方法，有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
    
    请试写一个死循环程序。
    
    """

sum_3 = 0
count = 0
while 1:
    sum_3 = sum_3 * sum_3 + 10086
    print "第%s次" % sum_3
















