#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#重构函数之想怎么加就怎么加
x=0
y=0
class complex():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if type(other)==type(self): #同类相加
            self.x+=other.x
            self.y+=other.y
        elif type(other) == type(10):#数据相加
            self.x=self.x+ other

        print(self.x, "+", self.y, "j")
c1=complex(3,4)
c2=complex(5,6)
c=c1+c2
cnum=c1+8






