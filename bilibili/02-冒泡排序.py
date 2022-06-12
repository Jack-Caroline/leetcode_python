#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/12 上午11:37

# 复杂度为：O（n^2）

def BubbleSort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                num = li[j + 1]
                li[j + 1] = li[j]
                li[j] = num
                exchange = True
                print(li)
        if not exchange:
            return li


l1 = [1, 2, 3, 4, 5, 6, 11, 14, 13, 19]
l2 = BubbleSort(l1)
print(l2)
