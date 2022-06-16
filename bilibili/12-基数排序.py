#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/15 下午11:42

"""
基数排序
    先排个位、再排十位、再排百位，依次排下去；
    每次排完，再取数据，就是排好序了；
    时间复杂度：O(kn)
    空间复杂度：O(k+n)
        k 表示数字位数

"""


def RadixSort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        li.clear()
        for buc in buckets:
            # extend 一次性添加多个列表元素，列表形式
            li.extend(buc)
        it += 1
