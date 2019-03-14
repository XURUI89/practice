#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：写出阶层的类。
class 阶层():
    pass
    def __init__(self,num):
        self.num=num
        s=1
        for i in range(1,self.num):
            s+=s*i
            i+=1
        print(s)
阶层(6)