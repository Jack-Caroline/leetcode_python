#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/6/12 下午5:57

def SelectSort(li):
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
               li[i],li[j] = li[j],li[i]
        print(li)
    return li

l1 = [2,3,1,6,5,4,7,8,9,0]
l2 = SelectSort(l1)
print(l2)