#!/usr/bin/python
# -*- coding: utf-8 -*-


def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue


if __name__ == "__main__":
    alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]
    insertionSort(alist)
    print(alist)
