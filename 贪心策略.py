#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
问题：计算极为低效
"""


def recMC(coinVaueList, change):
    minCoins = change
    if change in coinVaueList:
        return 1
    else:
        for i in [c for c in coinVaueList if c <= change]:
            numCooins = 1 + recMC(coinVaueList, change - i)
            if numCooins < minCoins:
                minCoins = numCooins
    return minCoins


def recDC(coinVaueList, change, knownResults):
    minCoins = change
    if change in coinVaueList:
        # 递归最优解，记录
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinVaueList if c <= change]:
            numCoins = 1 + recDC(coinVaueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins


if __name__ == "__main__":
    # print(recMC([1, 5, 10, 25], 63))
    print(recDC([1, 5, 10, 25], 63, [0] * 64))
