#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
递归和栈有类似的地方，这里使用到辗转相除法
"""


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        # 最小规模
        return convertString[n]
    else:
        # 减小规模，调用自身，反向读写数据
        return toStr(n // base, base) + convertString[n % base]


print(toStr(1453, 16))
