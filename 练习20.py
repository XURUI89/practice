#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
from functools import reduce
l=[1,1]
除数序列=[]
for i in range(0,20):
    a=l[i+1]+l[i]
    l.append(a)
    b=l[i+1]
    除数序列.append(a/b)
    i+=1
print(除数序列)
求和 = reduce(lambda x,y : x + y,除数序列)
print ("计算和为：",求和)
'''
a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1,20):
    b,a = a,a + b
    l.append(a / b)
print reduce(lambda x,y: x + y,l)

'''
