#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/13 16:41

# 堆排序
# 堆排序的时间复杂度：O(nlogn)


def sift(li, low, hight):
    """
    :param li:列表
    :param low: 堆的根节点位置
    :param hight: 堆的最后一个元素的位置
    :return:
    """
    i = low  # 最开始指向根节点
    j = 2 * i + 1  # j 开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= hight:  # j 的位置不能大于堆最后一个元素的位置
        if j + 1 <= hight and li[j + 1] > li[j]:  # 判断右孩子是否大于堆最后一个元素位置，并且是否大于左孩子
            j = j + 1
        if li[j] > tmp:  # 判断 j 位置的数据，是否大于 i 位置的数据
            li[i] = li[j]  # 如果大于，将 j 位置，移动到 i 位置
            i = j  # 将 j 赋值给 i
            j = 2 * i + 1  # 将 j 向下移动到左孩子
        else:
            li[i] = tmp  # 如果小于，将 tmp 的数据，赋值到 j 位置，结束循环
            break
    else:
        li[i] = tmp


def HeapSort(li):
    # 创建堆，所有父结点都大于孩子结点
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)

    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
