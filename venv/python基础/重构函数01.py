#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#重构函数
x=0
y=0
class complex():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        self.x+=other.x
        self.y+=other.y
        print(self.x, "+", self.y, "j")
c1=complex(3,4)
c2=complex(5,6)
c=c1+c2
##这样最好的理解是
print(1+1)
print("1"+"2")
#只有在同类的情况下才可以修改




