#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
盘片塔，一共三根柱子。
让盘片最后从小到大，在第三根柱子摞起来。
2**n-1 次数
"""


count = []


def moveDisk(disk, fromPole, toPole):
    count.append(disk)
    print(f"moving disk[{disk}] from {fromPole} to {toPole}")


def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)


if __name__ == "__main__":
    moveTower(5, "#1", "#2", "#3")
    print(len(count))
