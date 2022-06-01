#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/3/3 16:30
"""
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

示例 1：
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例3：
输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

提示：
1 <= s.length<= 20
1 <= p.length<= 30
s只包含从a-z的小写字母。
p只包含从a-z的小写字母，以及字符.和*。
保证每次出现字符* 时，前面都匹配到有效的字符

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        cache[0][0] = True
        for i in range(1,len(p)):
            cache[i+1][0]=cache[i-1][0] and p[i]=='*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i]=="*":
                    cache[i+1][j+1]=cache[i][j+1] or cache[i-1][j+1]
                    if p[i-1]==s[j] or p[i-1]=='.':
                        cache[i+1][j+1] |= cache[i+1][j]
                else:
                    cache[i+1][j+1]=cache[i][j] and (p[i]==s[j] or p[i]=='.')
        return cache[-1][-1]