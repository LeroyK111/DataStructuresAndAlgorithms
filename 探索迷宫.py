#!/usr/bin/python
# -*- coding: utf-8 -*-

from shlex import join
import sys
import turtle as t
import random
import time
"""
使用矩阵创建迷宫.

寻找方向避免无限递归的死循环,需要用到面包屑。


"""

sys.set_coroutine_origin_tracking_depth = 100000000000




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
                        # !找到出发点，记路它的位置
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
        t.speed(0)

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
                    # !将墙砖坐标加入
                    self.walltTile.append((penIndex[0] + 5, penIndex[1] - 5))
                penIndex[0] += 10
                t.pu()
                t.goto(*penIndex)
                t.pd()
            penIndex[1] -= 10






    def searchPath(self):
        # 获取当前朝向
        currentHead = t.heading()
        
        # 直接在当前朝向上前进一步
        t.fd(10)
        # 获取当前位置
        currentPosition = tuple(map(lambda x: round(x, 1), t.pos()))
        
        
        a = random.choice([-1, 1])
        
        # ?判断是否在墙内
        if currentPosition in self.walltTile:
            # ?在墙内，则后退一步，递归调用本方法
            t.bk(10)
            t.rt(90 * a)
            self.searchPath()
        elif currentPosition in self.passing:
            t.rt(90 * a)
            self.searchPath()
        else:
            # ?不在墙内，则判断是否在四周墙壁的出口上。
            if currentPosition[0] in [5, 255] or currentPosition[1] in [-5, -85]:
                # ?在出口,则停止递归，标记自己走来的路
                t.fillcolor("red")
                self.passing.append(currentPosition)
                self.passing.reverse()
                self.outletMarker()
            else:
                # ?不在出口，则递归调用本方法。
                if currentPosition not in self.passing:
                    self.passing.append(currentPosition)
                self.searchPath()
                
    def outletMarker(self): 
        # ?绘制迷宫路径图, 还可以继续优化，消除冗余路径。
        for index in self.passing:
            t.goto(*index)
            t.stamp()
    
        print("Outer Marker")
    

    def run(self):
        # 画迷宫地图
        self.plotMap()

        # 回到初始位置
        t.st()
        t.pu()

        t.home()
        self.startRow = self.startRow * -10 - 5
        self.startCol = self.startCol * 10 + 5
        t.goto(self.startCol, self.startRow)
        # 创建已经走过路径数组
        self.passing = []
        # 记录起始点的位置
        self.passing.append(t.pos())
        
        self.searchPath()

        t.exitonclick()
        


if __name__ == "__main__":
    demo = Maze("learning/机器学习/自学算法/DataStructuresAndAlgorithms/maze.txt")
    
 
    demo.run()

    
    # demo.test()
    
    
