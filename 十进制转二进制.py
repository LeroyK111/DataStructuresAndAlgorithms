#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.basic.stack import Stack

"""
辗转相除法。
"""


def divideBy2(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        # 余数放入栈
        remstack.push(rem)
        # 取整数
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString += digits[remstack.pop()]

    return binString


print(divideBy2(42, 16))
