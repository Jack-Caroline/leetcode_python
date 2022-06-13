#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/13 10:16
"""
快速排序：
思路：
    取一个元素P 第一个元素，使元素p归为
    列表被p分成两部分，左边都比p小，右边都比p大
    递归完成排序
时间复杂度：O(nlogn)，最坏情况：O(n^2)

"""


def Partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def QuickSort(li, left, right):
    if left < right:
        mid = Partition(li, left, right)
        QuickSort(li, left, mid - 1)
        QuickSort(li, mid + 1, right)
