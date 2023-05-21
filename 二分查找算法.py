#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
二分查找,  也适合动分而治之
"""


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midPoint = (first + last) // 2
        if alist[midPoint] == item:
            found = True
        else:
            if item < alist[midPoint]:
                last = midPoint - 1
            else:
                first = midPoint + 1

    return found


if __name__ == "__main__":
    testlist = [1, 2, 3, 5]
    print(binarySearch(testlist, 2))
