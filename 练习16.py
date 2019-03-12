#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
from functools import reduce
l = []
def sum(a):
    for i in range(1,10):
        k=a/2
        l.append(k*2)
        i+=1
        a=k
sum(100)
def f(x,y):
    return x+y
print("在第10次落地时，共经过多少米{0}".format(float(reduce(f,l))+100))
print(l[8])
print("第10次反弹多高{0[8]}".format(l))


