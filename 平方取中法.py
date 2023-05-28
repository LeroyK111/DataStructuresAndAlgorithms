#!/usr/bin/python
# -*- coding: utf-8 -*-


def middleSquareMethod(data, slot):
    data = str(data**2)
    middleEnd = len(data) // 2
    middleStart = middleEnd - 1
    result = int(data[middleStart] + data[middleEnd])
    # 开始进行散列函数
    index = result % len(slot)
    slot[index] = data
    return slot


if __name__ == "__main__":
    data = 44
    slot = [None for _ in range(11)]
    result = middleSquareMethod(data, slot)
    print(result)
