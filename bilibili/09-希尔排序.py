#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/15 11:07
"""
希尔排序
    Shell Sort 是一种分组插入排序算法。
    首先取一个整数 d1=n/2，将元素分为 d1 个组，每组相邻量元素之间距离为 d1，在各组内进行直接插入排序；
    取第二个整数 d2=d1/2，重复上述分组排序过程，直到 d1=1，即所有元素在同一组内进行直接插入排序；
    希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。

"""
from bilibili.calc_time import calc_time

def InsertSortGap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

@calc_time
def ShellSort(li):
    d = len(li) // 2
    while d >= 1:
        InsertSortGap(li, d)
        d //= 2

li=list(range(1000))
import random
random.shuffle(li)
ShellSort(li)
print(li)