#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

输入一行字符=input("请输入任意数据：")


数字个数=len(list(i for i in 输入一行字符 if i.isdigit()==1))
中英文字母个数=len(list((i for i in 输入一行字符 if i.isalpha()==1)))
空格个数=len(list(i for i in 输入一行字符 if i==" "))
其他个数=len(输入一行字符)-数字个数-中英文字母个数-空格个数
print("{0}中有{1}个数字，{2}个中英文字母，{3}个空格个数，{4}个其他".format(输入一行字符,数字个数,中英文字母个数,空格个数,其他个数))











