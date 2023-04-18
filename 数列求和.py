#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
不使用循环的情况下，只使用递归进行求和
"""


def listnum(numlist):
    print(numlist)
    if len(numlist) == 1:
        # 最小规模
        return numlist[0]
    else:
        # 减少规模
        return numlist[0] + listnum(numlist[1:])


print(listnum([1, 2, 3, 4, 5]))
