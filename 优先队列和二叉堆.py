#!/usr/bin/python
# -*- coding: utf-8 -*-
from pythonds.trees.binheap import BinHeap


class Solution(object):
    def run(self):
        self.bh = BinHeap()
        self.bh.insert(5)
        self.bh.insert(1)
        self.bh.insert(8)
        self.bh.insert(11)

    def reads(self):
        print(self.bh.delMin())
        print(self.bh.delMin())
        print(self.bh.delMin())
        print(self.bh.delMin())
        

if __name__ == "__main__":
    sl = Solution()
    sl.run()
    sl.reads()
