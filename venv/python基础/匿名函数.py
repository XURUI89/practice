#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#重构函数
x=0
y=0
class complex():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def  show (self):
        print(self.x, "+", self.y, "j")

    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)
c1=complex(3,4)
c2=complex(5,6)
c=c1+c2
##这样最好的理解是
print(1+1)
print("1"+"2")
#只有在同类的情况下才可以修改

#上面的c1,c2是有名对象
#直接调用不传递给某个值就是匿名对象
print((complex(3,4).show()))
c3=c1+c2
complex.show(c3)
c4=c1.__add__(c2)
complex.show(c4)



