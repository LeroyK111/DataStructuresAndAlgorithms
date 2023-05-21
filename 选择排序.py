#!/usr/bin/python
# -*- coding: utf-8 -*-


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


if __name__ == "__main__":
    alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]
    selectionSort(alist)
    print(alist)
