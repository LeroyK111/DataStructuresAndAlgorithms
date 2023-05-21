#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
典型的 平方阶O(n^2)
"""


def bubbleSort(alist):
    exchanges = True

    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        passnum = passnum - 1


if __name__ == "__main__":
    alist = [54, 26, 25, 17, 56, 78]
    # bubbleSort(alist)
    shortBubbleSort(alist)
    print(alist)
