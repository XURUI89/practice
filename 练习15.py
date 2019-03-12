#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
from functools import reduce
def zhiyingshu():
    for s in range(2,1000):
        l = []
        for i in range(1,s):
            if s%i==0:
                l.append(i)
                i+=1
        def f(x, y):
            return x + y
        sum=reduce(f,l)
        if sum == s:
            print(s,list(l))
        s+=1
zhiyingshu()







