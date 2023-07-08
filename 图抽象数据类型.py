#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.graphs.adjGraph import Graph


g = Graph()
for i in range(6):
    g.addVertex(i)


# 获取列表结构
print(g.vertices)

# 在各个节点之间的边，插入权重
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)" % (v.getId(), w.getId()))


