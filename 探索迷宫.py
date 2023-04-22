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
        
    
    
    
    
        
        
        
    
    


if __name__ == "__main__":
    demo = Maze("learning/机器学习/自学算法/DataStructuresAndAlgorithms/maze.txt")
    demo.test()



