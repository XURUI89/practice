#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：输出指定格式的日期。
from datetime import datetime
日期输入=input("请输入日期（xxxx/xx/xx)：")##这是要求输入的格式，可以根据情况调整
提取日期=datetime.strptime(日期输入,"%Y/%m/%d")
输出日期=m=print(提取日期.strftime("%Y--%m--%d"))##这是要求输出的格式，可以根据情况调整
