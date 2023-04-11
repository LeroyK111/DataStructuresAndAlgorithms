#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.basic.deque import Deque


def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True
    if chardeque.size() % 2 != 0:
        return "非偶数，不推荐使用双端队列解决"

    while chardeque.size() > 0 and stillEqual:
        # 从两边向中间递进比较，然后就知道是不是对称回文了
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker("lst1tsl"))
