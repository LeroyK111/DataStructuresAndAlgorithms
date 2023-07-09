#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
! 如何将大量的单词放入到图中：
1.将单词作为顶点的key，如果两个单词之间只相差一个字母，就在他们之间设置一条边
2.无向图==顶点之间没有权重
"""
from pythonds.graphs.adjGraph import Graph
from pythonds.basic.queue import Queue
import os


def buildGraph(wordFile):
    d = {}
    g = Graph()
    # 获取四字母单词集
    wfile = open(wordFile, "r")
    for line in wfile:
        word = line.strip()
        for i in range(len(word)):
            bucket = word[:i] + "-" + word[i + 1 :]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g


# BFS算法
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    # 设置队列
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        # 取队首作为当前顶点
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            # 遍历临街顶点
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            # 设置当前顶点为黑色
            currentVert.setColor("black")


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == "__main__":
    xpth = os.path.dirname(os.path.abspath(__file__))
    os.chdir(xpth)
    wordgraph = buildGraph("./word.txt")
    bfs(wordgraph, wordgraph.getVertex("FOOL"))
    traverse(wordgraph.getVertex("SAGE"))
