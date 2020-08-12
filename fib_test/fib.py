#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/12 10:45
#!@Author: Zhang-sl

def fib(n):
    fibs = [1,1]
    if n<1:
        return None
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs