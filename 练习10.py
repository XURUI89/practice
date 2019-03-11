#!/usr/bin/env python 
# -*- coding:utf-8 -*-
    #题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
num=int(input("请输入一个正整数:"))
t=num    #可以保持num在范围上不改变
s=[]
def l(num):

    for i in range(2,t+1):
        if num%i==0:
            s.append(i)
            return l(num/i)
l(num)
输出合并 = '*'.join(str(x) for x in s)
print("{0}={1}".format(num, 输出合并))
print("如果返回原值，表示只能被自己整除")


















