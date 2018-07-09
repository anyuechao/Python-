#!/usr/bin/env python
#coding=utf-8

import chardet

'''
	使用chardet
	'''
import re

chardetList =  dir(chardet) 
chlist = []
for x in chardetList:
	if (re.match(r'[a-zA-Z]{0,100}$',x)):
		chlist.append(x)

# print('chardet属性：',chlist)
'''['UniversalDetector', 'VERSION', 'chardistribution', 'charsetgroupprober', 'charsetprober', 'codingstatemachine', 'compat', 'detect', 'enums', 'escprober', 'escsm', 'eucjpprober', 'euckrfreq', 'euckrprober', 'euctwfreq', 'euctwprober', 'hebrewprober', 'jisfreq', 'jpcntx', 'langbulgarianmodel', 'langcyrillicmodel', 'langgreekmodel', 'langhebrewmodel', 'langthaimodel', 'langturkishmodel', 'mbcharsetprober', 'mbcsgroupprober', 'mbcssm', 'sbcharsetprober', 'sbcsgroupprober', 'sjisprober', 'universaldetector', 'version']'''


'''
	当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
	'''
r1 = chardet.detect(b'Hello,world!')
print('检测编码1:',r1)
'''
	{'encoding': 'ascii',#编码格式
	'confidence': 1.0, #检测的概率1.0(即100%)
	'language': ''
	}

	'''

'''
	我们来试试检测GBK编码的中文：
	'''
# data = '大风起兮,云飞扬'.encode('gbk') 
data = '离离原上草，一岁一枯荣'.encode('gbk') 

r2 = chardet.detect(data)
print('检测编码2-GBK编码:',r2)
'''
	{
	'encoding': 'IBM855',
    'confidence': 0.5266078104422526,
    'language': 'Russian'
    }
	'''
data1 = '大厦将倾，谁堪栋梁'.encode('utf-8')
r3 = chardet.detect(data1)
print('检测编码2-UTF-8编码:',r3)

# 日文检测
data2 = '最新の主要ニュース'.encode('euc-jp') 
r4 = chardet.detect(data2)
print('检测编码2-日文编码:',r4)









