#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#一个整数，它加上 100 后是一个完全平方数，再加上 268 又是一个完全平方数，请问该数是多少？
'''

for i in range(1000):
    for n in range(1000):
        for m in range(1000):
            if i+100==m*m and i+268==n*n:
                print(i,m,n)
                continue

#虽然也有结果，但这样写太慢了


'''

import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100)and (y*y==i+268):
        print (i)
#这样就快很多，几乎只要几秒钟