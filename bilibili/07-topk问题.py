#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/14 16:38
"""
堆排序-topk问题
    现在有 n 个数，设计算法得到前 k 大的数。（k<n）
解决思路：
    排序后切片         O(nlogn)
    排序 LowB 三人组(冒泡、选择、插入)   O(kn)
    堆排序            O(nlogk)
        取列表前 k 个元素简历一个小根堆。堆顶就是目前第 k 大的数。
        依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为元素，并且对堆进行一次调整，
        遍历列表所有元素后，倒序弹出堆顶；
"""
import random


def sift(li, low, hight):
    """
    建立小根堆
    :param li:列表
    :param low: 堆的根节点位置
    :param hight: 堆的最后一个元素的位置
    :return:
    """
    i = low  # 最开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= hight:  # j 的位置不能大于堆最后一个元素的位置
        if j + 1 <= hight and li[j + 1] < li[j]:  # 判断右孩子是否大于堆最后一个元素位置，并且是否大于左孩子
            j = j + 1
        if li[j] < tmp:  # 判断 j 位置的数据，是否大于 i 位置的数据
            li[i] = li[j]  # 如果大于，将 j 位置，移动到 i 位置
            i = j  # 将 j 赋值给 i
            j = 2 * i + 1  # 将 j 向下移动到左孩子
        else:
            li[i] = tmp  # 如果小于，将 tmp 的数据，赋值到 j 位置，结束循环
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    # 建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 遍历
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


li = list(range(1000))
# 打乱顺序
random.shuffle(li)
print(li[0:10])
print(topk(li, 10))
