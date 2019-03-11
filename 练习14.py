#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
from functools import reduce
a=int(input("几次重复加："))
b=int(input("想要重复的数字是："))
s=[]
tn=0
#sum=b*a*10+b*(a-1)*10+…………+b*1*10
for count in range(0,a):
    tn=tn+b
    b=10*b
    s.append(tn)
    print(tn)
s = reduce(lambda x,y : x + y,s)
print ("计算和为：",s)








