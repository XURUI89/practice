#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
def 水仙花数():

    for i in range(100,1000):
       百位数= i//100
       十位数=i%10
       个位数=(i%100-十位数)/10
       if i==百位数**3+个位数**3+十位数**3:
           print(i)
           i+=1
           continue

水仙花数()


