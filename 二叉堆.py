#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def __init__(self) -> None:
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                # 与父节点交换位置
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            # 沿路经向下
            i = i // 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                # 交换下沉
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            # 唯一子节点
            return i * 2
        else:
            # 返回较小的

            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        """
        当你移除根节点时，为了保持二叉树的完整性，只能用最后一个节点代替根节点。下沉路径的选择。
        """
        # 移走堆顶
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # 新顶下沉
        self.percDown(1)
        return retval

    def insert(self, key):
        """
        !新key加载队表末尾，显然无法保持“堆”次序，虽然对其他路径的次序没有影响，但对于其到根路径可能破坏次序。
        """
        # 添加到末尾
        self.heapList.append(key)
        self.currentSize += 1
        # 新key上浮
        self.percUp(self.currentSize)

    def buildHeap(self, alist):
        # 从无序表生成堆，这里从父节点下沉法
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while i < 0:
            print(self.heapList[i], i)
            self.percDown(i)
            i -= 1
        print(self.heapList, i)


if __name__ == '__main__':
    D = Demo()
    D.insert(123)
    D.insert(13)
    D.insert(12)
    D.insert(1)

    print(D.delMin())
    print(D.delMin())
    print(D.delMin())
    print(D.delMin())

    
        
    