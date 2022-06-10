#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/1 上午10:24

def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" %(a,c))
        hanoi(n-1, b, a, c)

hanoi(3, 'A', 'B', 'C')

