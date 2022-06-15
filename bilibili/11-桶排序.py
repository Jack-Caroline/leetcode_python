#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/15 16:50
"""
桶排序
    在计数排序中，如果元素范围比较大（比如在 1-1亿 之间），计数排序占用空间比较大，需要优化算法；
    桶排序（Bucket Sort）：首先将元素分在不同的桶中，在对每个桶中的元素排序；
    桶排序的表现取决于数据的分布。也就是需要对不同数据排序时采取不同的分桶策略；
    平均情况时间复杂度：O(n+k)
    最坏情况时间复杂度：O(n^2*k)
    空间复杂度：O(nk)
"""


def BucketSort(li, n=100, max_num=10000):
    # 生成100个桶（列表中100个空列表）
    buckets = [[] for _ in range(n)]
    for var in li:
        # 将 li 遍历的数据，选择放在哪个桶里，max_num // n 判断每个桶的范围，var 对范围整除；考虑到最后一个数整出后找不到桶则与最后一个桶比较取最小；
        i = min(var // (max_num // n), n - 1)
        buckets[i].append(var)
        for j in range(len(buckets[i] - 1), 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sort_li = []
    for buc in buckets:
        sort_li.extend(buc)
    return sort_li
