#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle as t
import random

"""
使用矩阵创建迷宫.

寻找方向避免无限递归的死循环,需要用到面包屑。
"""


class Maze:
    def __init__(self, filePath) -> None:
        rowsInMaze = 0
        self.mazelist = []
        with open(filePath, "r", encoding="utf-8") as f:
            for line in f.readlines():
                rowList = []
                col = 0
                for ch in line[:-1]:
                    # 读取一行中的每列
                    rowList.append(ch)

                    if ch == "S":
                        # 找到出发点，记路它的位置
                        self.startRow = rowsInMaze
                        self.startCol = col

                    # 列坐标+1
                    col += 1
                # 行坐标+1
                rowsInMaze += 1
                # 最后将每一行加入到列表中
                self.mazelist.append(rowList)

    def test(self):
        print(len(self.mazelist[0]))
        print(len(self.mazelist))
        print(self.mazelist)
        print(self.startRow, self.startCol)

    def plotMap(self):
        t.screensize(1000, 1000, None)
        # 设置画笔初始坐标
        t.setx(0)
        t.sety(0)
        # 画笔形状
        t.shape("turtle")
        t.shapesize(0.5, 0.5)
        # 隐藏/展示画笔形状
        t.ht()
        # t.st()
        # 画笔颜色，填充颜色
        t.color("black", "orange")
        t.speed(100000)

        # 创建墙壁坐标
        self.walltTile = []

        penIndex = [0, 0]
        # 开始作画
        for row in self.mazelist:
            penIndex[0] = 0
            t.pu()
            t.goto(*penIndex)
            t.pd()
            for col in row:
                if "+" == col:
                    t.begin_fill()
                    t.fd(10)
                    t.right(90)
                    t.fd(10)
                    t.right(90)
                    t.fd(10)
                    t.right(90)
                    t.fd(10)
                    t.right(90)
                    t.end_fill()
                    # 将墙砖坐标加入
                    self.walltTile.append((penIndex[0] + 5, penIndex[1] - 5))
                penIndex[0] += 10
                t.pu()
                t.goto(*penIndex)
                t.pd()
            penIndex[1] -= 10

    def searchPath(self, oldHead=0):
        # 获取当前朝向
        currentHead = t.heading()

        # 直接在当前朝向上前进一步
        t.fd(10)

        # 获取当前位置
        currentPosition = tuple(map(lambda x: round(x, 1), t.pos()))

        # 判断是不是在墙内
        if currentPosition in self.walltTile:
            t.bk()
            self.searchPath(oldHead=currentHead)

        # 判定当前位置出口, 是否在四个墙边，并且不属于墙内
        if currentPosition[0] in [5, 255] and currentPosition[1] in [-5, -85] and currentPosition not in self.walltTile:
            return "找到出口"
        else:
            t.bk()
            t.right(90)
            self.searchPath()

    def run(self):
        # 画迷宫地图
        self.plotMap()

        # 回到初始位置
        t.st()
        t.pu()

        t.fillcolor("red")
        t.home()
        t.goto(self.startCol * 10 + 5, self.startRow * -10 - 5)

        # 计算路径
        self.searchPath()

        t.exitonclick()


if __name__ == "__main__":
    demo = Maze("learning/机器学习/自学算法/DataStructuresAndAlgorithms/maze.txt")
    demo.run()
    # demo.test()
