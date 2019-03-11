#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#输入三个整数x,y,z,把这个数由大到小输出

import mmap
x=int(input("please input 1 number: "))
y=int(input("please input 1 number: "))
z=int(input("please input 1 number: "))
s=[x,y,z]
t=sorted(s,reverse=True)#sorted(数列，key=abs,reverse=Ture)
print(t)




