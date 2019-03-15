#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#题目：有5个人坐在一起，问第五个人多少岁？
# 他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第3个人，又说比第2人大两岁。
# 问第2个人，说比第1个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
s=10
for i in range(0,4):
    s=s+2
print(s)
print("*"*80)

#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
输入数字=str(input("your numbers: "))
n=len(输入数字)
s=(输入数字[i] for i in range(n-1,-1,-1))
l=list(s)
print("逆序排：",l)
print("是{0}位数".format(n))
w=['个位：','十位','百位','千位','万位','十万位']
for i in zip(w,list(l)):
    print(i,end=" ")
print("\n")
print("*"*80)
#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
输入数字2=str(input("your numbers: "))
n=len(输入数字2)
flag=True
for i in range(0,int(n/2)+1):
    if 输入数字2[0+i]!=输入数字2[n-i-1]:
        flag=False
if flag==True:
    print("是回文")
else:
    print("不是回文")
print("*" * 80)
#题目：按逗号分隔列表。
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print (s1)
print("*" * 80)
#题目：文本颜色设置。
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)












