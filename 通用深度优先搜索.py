#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.graphs import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor("gray")
        self.time += 1
        startVertex.setDiscovery(startVertex)
        for nextVertex in startVertex:
            if nextVertex.getColor() == "white":
                nextVertex.setPred(-1)
                self.dfsvisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.finish)
