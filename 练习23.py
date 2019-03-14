#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

a=str(input("no.1"))
b=str(input("no.2"))
c=str(input("no.3"))
d=str(input("no.4"))
e=str(input("no.5"))
l=[a,b,c,d,e]
for i in range(0,5):
    for n in range(0,5):
        if l[i]>l[n]:
            l[i],l[n]=l[n],l[i]
        else:
            l[i], l[n] = l[i], l[n]
print(l)

'''
def output(s, l):
    if l == 0:
        return
    print(s[l - 1],end=" ")
    output(s, l - 1)


s = str(list('Input a string:'))
l = len(s)
output(s, l)

'''




