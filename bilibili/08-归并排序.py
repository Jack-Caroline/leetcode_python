#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/14 17:19
"""
归并排序
    假设现在的列表分两段有序，如何将其合并成一个有序列表？
        将两段列表逐个进行比较，小的拿出来，最后合并成一个列表叫做归并；
    分解：将列表越分越小，直至分成一个元素
    终止条件：一个元素是有序的
    合并：将两个有序列表归并，列表越来越大；
时间复杂度：O(nlogn)
空间复杂度：O(n)

"""


def Merge(li, low, mid, high):
    i = low
    j = mid + 1
    l = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            l.append(li[i])
            i += 1
        else:
            l.append(li[j])
            j += 1
    while i <= mid:
        l.append(li[i])
        i += 1
    while j <= high:
        l.append(li[j])
        j += 1
    return l


# li = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16]
# print(Merge(li, 0, 4, 12))


def MergeSort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(li, low, mid)
        MergeSort(li, mid + 1, high)
        Merge(li, low, mid, high)
