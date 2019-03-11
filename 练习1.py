#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#利用random函数，生产0-100直接的整数
def suijishu():
    import random
    print("{0}".format(int(random.random()*100)))

suijishu()

def suijishu1():
    import random
    print(random.randint(1, 100))
suijishu1()
