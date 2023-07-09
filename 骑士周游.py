#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.graphs.adjGraph import Graph


def genLegalMoves(x, y, bdSize):
    newMoves = []
    # 马的八种走法
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))

        return newMoves


def legalCoord(x, bdSize):
    # 确认不走出棋盘
    if x >= 0 and x <= bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        # 遍历每个格子
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            # 单步合法走棋
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                # 添加边及顶点
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


def knightTour(n, path, u, limit):
    # n层次，path路径，u顶点，limit深度
    u.setColor("gray")
    # 当前顶点加入路径
    path.append(u)

    if n < limit:
        # 对所有合法移动逐一深入
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            # 选择白色未经过顶点深入
            if nbrList[i].getColor() == "white":
                # 层次加一，递归深入
                done = knightTour(n + 1, path, nbrList[i], limit)
                i += 1
        if not done:
            # 都无法完成总深度，回溯，试本层下一个顶点
            path.pop()
            u.setColor("white")
    else:
        done = True
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]
