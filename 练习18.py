#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

teamA=["a","b","c"]
teamB=["x","y","z"]
s=((a,b) for a in teamA for b in teamB )
l=[("a","x"),("c","x"),("c","z")]
print(list(set(s)^set(l)))#打散再组合



