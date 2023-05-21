#!/usr/bin/python
# -*- coding: utf-8 -*-


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def partition(alist, first, last):
    # 选定中值
    pivotValue = alist[first]

    # 左右标初值
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        
        # 向右移动左标
        while leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1

        # 向左移动右标
        while alist[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark -= 1

        # 两标相错，结束移动
        if rightMark < leftMark:
            done = True
        else:
            # 左右标的值交换
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

    # 中间值就位
    alist[first], alist[rightMark] = alist[rightMark], alist[first]

    # 中间值点，分裂点
    return rightMark


def quickSortHelper(alist, first, last):
    # 基本结束条件
    if first < last:
        # 分裂
        splitPoint = partition(alist, first, last)
        # 递归调用
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


if __name__ == "__main__":
    alist = [54, 26, 25, 17, 56, 78]
    # bubbleSort(alist)
    quickSort(alist)
    print(alist)
