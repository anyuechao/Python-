#!/usr/bin/env python
#coding=utf-8

"""1.list数组
    Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
    比如，列出班里所有同学的名字，就可以用一个list表示：
    """
classmates =['Michael' , 'Bob', 'Tracy']
for i in classmates:
    print ("%s是咱们班的学生" % i)
    print ("{0}是咱们班的学生".format(i))

print("咱班一共有%s人" % len(classmates))

'''1.1 查
    访问list中每一个元素的位置
    访问list中每一个位置的元素
    
    list 越界
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    '''

print("第一位同学{0}".format(classmates[0]))
print("最后一个同学为%s" % classmates[len(classmates) - 1])
print("最后一个同学为%s" % classmates[ - 1])
print("倒数第二个同学为%s" % classmates[ - 2])

'''1.2增
    list是一个可变的有序表，所以，可以往list中追加元素到末尾：
    '''
classmates.append('admin')
classmates.insert(1,'Jack')

'''1.3删
    要删除list末尾的元素，用pop()方法：
    要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
    '''
classmates.pop()
classmates.pop(1)

'''1.4改
    要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
    '''
classmates[1] = 'Sarah'

'''1.5
    '''
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
#list元素也可以是另一个list，比如：
S =['Python','java',['asp','php'],'scheme']
len(S)
#要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
d = ['asp','php']
S =['Python','java',d,'scheme']
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
print ("拿到数组list中的索引为2的list的所因为1的元素"s[2][1])

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L = []
len(L)


"""2.tuple元组
    另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
    
    现在，teammates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用teammates[0]，teammates[-1]，但不能赋值成另外的元素。
    不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
    tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
    """
teammates = ('Jake','YuechaoAn','XinxinG')
t = (1,2)

'''2.1 tuple中()与数学符号()的相似性如何避免
    定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
    
    所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
    Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
    '''
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t_1 = (1,)
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
print (t_1)

'''2.2 “可变的”tuple：
    '''
l_1 = ['A','B']
t_2 = ('a','b',l_1)
print t_2
l_1.pop()

'''2.3
    tuple 的不可变性指的是他的元组指向不可改变
    
    表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
    
    理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
    '''
"""3.小结
    list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
    
    """



