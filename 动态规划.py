#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
叠加过程能保持最优解的关键是，其依赖于更少钱数最优解的简单计算，而更少钱数的最优解已经得到了。
问题的最优解包含了更小子规模问题的最优解，这是一个最优化问题能够用动态规划策略解决的必要条件。

! 最简单的情况开始，每一步都对前一步的结果有依赖。
"""


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # 从1分开始到change，逐个计算最少的硬币数
    for cents in range(1, change + 1):
        # 初始化一个最大值
        coinCount = cents
        newCoin = 1
        # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 得到最少的硬币数，记录到表中
        minCoins[cents] = coinCount
        # 记录本步骤加的一个硬币
        coinsUsed[cents] = newCoin

    # 返回最后一个结果
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


if __name__ == "__main__":
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    dpMakeChange(clist, amnt, coinCount, coinsUsed)
    printCoins(coinsUsed, amnt)
    # print(coinsUsed)
