#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#求1+2!+3!+...+20!的和。
from functools import reduce
sum=[]
for i in range(1,21):
    a=1
    l = []
    while a<=i:
        l.append(a)
        a+=1
    每个阶层 = reduce(lambda x, y: x*y, l)
    sum.append(每个阶层)
求和 = print(reduce(lambda x, y: x+y, sum))
'''
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print(s)

'''






