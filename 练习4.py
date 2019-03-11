#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#输入某年某月某日，判断这一天是这一年的第几天


from datetime import datetime


n1=input("please input your date(年-月-日）: ")
OutPutDay=datetime.strptime(n1,"%Y-%m-%d")


m=print(OutPutDay.strftime("NO.%j"))



