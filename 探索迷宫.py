#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle


"""
使用矩阵创建迷宫.

寻找方向避免无限递归的死循环,需要用到面包屑。
"""


class Maze:
    def __init__(self, filePath) -> None:
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        with open(filePath, "r", encoding="utf-8") as f:
            for line in f.readlines():
                rowList = []
                col = 0
                for ch in line[:-1]:
                    rowList.append(ch)
                    if ch == "S":
                        self.startRow = rowsInMaze
                        self.startCol = col
                    col += 1
                rowsInMaze += 1
                self.mazelist.append(rowList)
                columnsInMaze = len(rowList)

    def test(self):
        print(len(self.mazelist[0]))
        print(self.startRow, self.startCol)


    def plot(self, t):
        """
        假如每个*的面积都是1*1，则行高单位为1，列宽单位为1。
        """
        
        rowNumber = 0
        for row in self.mazelist:
            wallList = list(row)
            rowNumber +=1
            colNumber = 0
            for wallBrick in wallList:
                colNumber += 1
                # 记的加块砖
                
                
                
                
        t.done()        
                
        
        


    def run(self):
        # 海龟画图
        t = turtle.Turtle()
        self.plot(t)
        
        




if __name__ == "__main__":
    demo = Maze("learning/机器学习/自学算法/DataStructuresAndAlgorithms/maze.txt")
    demo.run()
    
    
    
