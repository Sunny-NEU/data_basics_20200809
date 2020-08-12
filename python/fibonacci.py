#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/6 19:36
#!@Author: Zhang-sl
def fibo(n):
    res=[1,1,2]
    while len(res)<n:
        res.append(res[-1]+res[-2])
    return res