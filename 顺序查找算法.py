#!/usr/bin/python
# -*- coding: utf-8 -*-


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True

        else:
            pos += 1

    return found


if __name__ == "__main__":
    # 无序表和有序表，区别仅在于，是否中途可以退出，减少计算次数。
    testList = [1, 2, 32, 8]
    print(sequentialSearch(testList, 32))
