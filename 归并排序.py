#!/usr/bin/python
# -*- coding: utf-8 -*-


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i += 1
            else:
                alist[k] = rightHalf[j]
                j += 1

            k += 1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j += 1
            k += 1


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)

    return merged


if __name__ == "__main__":
    alist = [2, 3, 1, 41, 24, 151, 2345, 3456, 234, 12345, 123, 32, 34]
    # mergeSort(alist)
    # print(alist)

    print(merge_sort(alist))
