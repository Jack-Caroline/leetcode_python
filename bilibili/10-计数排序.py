#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/15 15:52
"""
计数排序
问题：对列表进行排序，已知列表中的数范围都在 0-100 之间，设计时间复杂度为 O(n) 的算法。
"""


def CountSort(li, max_count=100):
    # _ 为占位符，不在意变量的值，循环遍历n次；
    # 表示生成长度为 max_count+1 ，值全部为 0 的序列；
    # 生成 100 个 0
    count = [0 for _ in range(max_count + 1)]
    # 根据遍历的数据，进行计数
    for val in li:
        count[val] += 1
    li.clear()
    print(count)
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


import random
li=[random.randint(0,100) for _ in range(1000)]
print(li)
CountSort(li,100)
print(li)