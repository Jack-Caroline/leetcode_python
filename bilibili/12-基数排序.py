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
    # it从0开始循环，每次加1，用于一次比较个位、十位、百位......
    it = 0
    # 最大数已经找到，用10的it次方，进行比较，当大于最大值时，停止循环；
    while 10 ** it <= max_num:
        # 生成10个桶，1到10，用于分装要素列表的要素
        buckets = [[] for _ in range(10)]
        for var in li:  # 遍历要素
            # 将要素对10的it次方相除取整后，然后对10取余数，得到digit为桶的key或者下标；
            digit = (var // 10 ** it) % 10
            # 添加要素到各个桶里
            buckets[digit].append(var)
        li.clear()
        for buc in buckets:
            # extend 一次性添加多个列表元素，列表形式
            # 将桶里的数据添加到li列表里，会从小到大排序
            li.extend(buc)
        it += 1
