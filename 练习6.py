#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#输出9*9乘法表
s=(i*n for i in range(1,10) for n in range(1,10))
print(list(s))