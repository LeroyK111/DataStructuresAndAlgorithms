#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
! 如何将大量的单词放入到图中：
1.将单词作为顶点的key，如果两个单词之间只相差一个字母，就在他们之间设置一条边
2.无向图==顶点之间没有权重
"""
from pythonds.graphs.adjGraph import Graph


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open("wordFile", "r")
    for line in wfile:
        word = line[:-1]
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


# 给定图g
