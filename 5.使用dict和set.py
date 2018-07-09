#!/usr/bin/env python
#coding=utf-8

"""1.dict
    dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
    
    举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
    
    """
#给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
names = ['Michael','Bob','Tracy']
scores = [95,75,85]
count = -1
for name in names:
    count = count + 1
    if name == "Bob":
        print scores[count]


#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = ['Michael']


























