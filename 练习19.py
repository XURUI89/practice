#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#打印出菱形

for n in range(1,8,2):
    空格数 = int((7 - n) / 2)
    星星数 = n
    print(空格数 * " ", 星星数 * "*", 空格数 * " ")
for m in range(5,0,-2):
    空格数 = int((7 - m) / 2)
    星星数 = m
    print(空格数 * " ", 星星数 * "*", 空格数 * " ")









