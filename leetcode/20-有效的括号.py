#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/7/11 14:44
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

"""

class Solution:
    def isValid(self, s):
        dict = {")": "(", "}": "{", "]": "["}    # 创建字典，括回为键，括号为值；
        stack = []    # 创建一个列表，模拟程堆栈
        for i in s:    # 循环读取 参数
            if stack and i in dict:   # 判断 stack 不为空，且 i 在字典的值中，如果在则为括回；
                if stack[-1] == dict[i]:  # 判断列表最后一个值，与字典中 括号，是否相同，相同则减去括号，否则为无效括号
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)  # 读取的字符串，不在字典中，则说明为括号，添加到列表中
        return not stack  # 最后读取字符串所有后，判断stack列表是否为空，如果为空则为False，not False 为 True


if __name__ == '__main__':
    s = "(()){({([(])})}{}[][])"
    solu = Solution()
    print(solu.isValid(s))