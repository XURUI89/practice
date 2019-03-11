#!/usr/bin/env python 
# -*- coding:utf-8 -*-
try:
    print("i love")
    print(3.1415926)
    #手动引发一个异常
    #注意语法：raise ErrorClassName
    raise ValueError
    print("还没完")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("我也不知道就出错了")
finally:
    print("我肯定会被执行")