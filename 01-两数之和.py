#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/2/23 9:33
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
"""


class Solution:
    # 方法一
    # def TowSum(self, nums: list, target: int):
    #     for i in nums:
    #         j = target - i
    #         start_index = nums.index(i)
    #         next_index = start_index + 1
    #         tump_nums = nums[next_index:]
    #         if j in tump_nums:
    #             list = []
    #             list.append(nums.index(i))
    #             list.append(next_index + tump_nums.index(j))
    #             return list

    # 方法二
    def TowSum(self, nums: list, target: int):
        dict = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j not in dict:
                dict[nums[i]] = i
            else:
                return (dict[j], i)


if __name__ == '__main__':
    nums1 = [3, 3]
    target1 = 6
    sum = Solution()
    print(sum.TowSum(nums1, target1))
