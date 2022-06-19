#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/19 下午1:29
""""""
"""
1、给两个字符串 s 和 t ，判断 t 是否为 s 的重新排序后组成的单词
    s = "anagram", t = "nagaram", return true
    s = "rat", t = "car", return falses

"""


def IsEqual(s, t):
    # 方式一：
    # ss = list(s)
    # tt = list(t)
    # ss.sort()
    # tt.sort()
    # return ss == tt
    # 方式二
    dict1 = {}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2


s = "nagaram"
t = "nagaram"
print(IsEqual(s, t))

"""
2、给定一个 m*n 的二位列表，查找一个数是否存在，列表属性；
    每一行的列表从左到右已经排序好；
    每一行第一个比上一行最后一个大；
"""


def searchMatrix(li, target):
    for i in li:
        if target in i:
            return True
    return False


li = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
target = 112
print(searchMatrix(li, target))

"""
3、给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数，保证肯定只有一个效果；
    例如：列表 [1,2,5,4] 与目标整数3，1+2=3，结果为 （0，1）
"""


def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    other = {}
    # enumerate 是读取列表index和value
    for k, v in enumerate(nums):
        if target - v in other:
            return [other[target - v], k]
        else:
            other[v] = k


nums = [2, 7, 11, 15]
target = 9
print (twoSum(nums, target))
