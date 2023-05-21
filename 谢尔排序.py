#!/usr/bin/python
# -*- coding: utf-8 -*-


def shellSort(alist):
    subListCount = len(alist) // 2
    while subListCount > 0:
        for startPosition in range(subListCount):
            gapInsertionSort(alist, startPosition, subListCount)

        subListCount = subListCount // 2


def gapInsertionSort(alist, startPosition, subListCount):
    for i in range(startPosition + subListCount, len(alist), subListCount):
        currentValue = alist[i]
        position = i
        while position >= subListCount and alist[position - subListCount] > currentValue:
            alist[position] = alist[position - subListCount]
            position = position - subListCount

        alist[position] = currentValue



if __name__ == '__main__':
    alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]
    shellSort(alist)
    print(alist)
    
    
    
    