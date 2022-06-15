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
