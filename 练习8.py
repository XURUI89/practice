#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：判断101-200之间有多少个素数，并输出所有素数。

#python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素
s=set(( n for n in range (101,201) for k in range (2,n) if n%k==0 ))
t=set((n for n in range(101,201)))
print(sorted(t-s))



#选取元组中的第一个值     res_list = [x for x,_ in s]
        #也可以           [x[0] for x in rows]
#对删除列表重复值         list1=sorted(set(res_list),key=res_list.index)
#打印列表                 print(list(list1))






