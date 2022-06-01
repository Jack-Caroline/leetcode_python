#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/3/3 16:32
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

"""


class Solution:
    def longestCommonPrefix(self, strs):
        # if not strs:
        #     return ""
        # for i in range(len(strs[0])):
        #     for string in strs[1:]:
        #         if i >= len(string) or string[i] != strs[0][i]:
        #             return strs[0][:i]
        # return strs[0]

        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as s:
                break
        return result
