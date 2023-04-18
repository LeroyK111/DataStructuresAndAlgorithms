#!/usr/bin/python
# -*- coding: utf-8 -*-


class OrderedNodeList:
    def __init__(self, item=None) -> None:
        self.head = None
        self.item = item

    def add(self, item):
        # ! 和无序表最大的区别，插入到某个节点之前，还要维护索引head，
        current = self.head
        prevous = None
        stop = False
        while current is not None and not stop:
            # 这里循序必须在第一个head赋值之前，
            if current.getValue() > item:
                stop = True
            else:
                prevous = current
                current = current.getNext()

        temp = OrderedNodeList(item)
        if prevous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            # 当前node设置head
            temp.setNext(current)
            # 前一个node设置head
            prevous.setNext(temp)

    def setValue(self, item):
        # 修改当前node的值
        self.item = item

    def getValue(self):
        # 获取当前node的值
        return self.item

    def getNext(self):
        # 获取下一个node
        return self.head

    def setNext(self, head):
        self.head = head

    def size(self):
        count = 0
        nextNode = self.head
        while nextNode is not None:
            nextNode = nextNode.getNext()
            count += 1
        return count

    def search(self, item):
        # 有序表的查找，则可以依靠大小来判定，节省搜索时间
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getValue() == item:
                # 当前值判断
                found = True
            else:
                if current.getValue() > item:
                    # 如果当前值已经大于item，则之后的node也是大于item的，有序链表从小到大
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        prevNode = None
        found = False

        """
        快慢指针: 思维误区，双指针才能实现地址的拼接, 但要排除第一个none
        """
        while not found:
            if current.getValue() == item:
                # 判断下一个指针的内容
                found = True
            else:
                prevNode = current
                current = current.getNext()

        if prevNode is None:
            self.head = current.getNext()
        else:
            prevNode.setNext(current.getNext())

    def pop(self, index=-1):
        # 移除并返回有序表中的指定位置
        # 默认最后一项
        index = self.size() - 1 if index == -1 else index
        count = 0
        current = self.head
        found = False
        while current is not None:
            if count == index:
                found = True
                break
            current = current.getNext()
            count += 1

        if found:
            res = current.getValue()
            self.remove(current.getValue())
            return res
        else:
            raise IndexError("Index not found")

    def isEmpty(self):
        if self.size() == 0:
            return False
        return True




if __name__ == "__main__":
    Demo = OrderedNodeList()
    for i in [3, 2, 1, 4]:
        Demo.add(i)

    for _ in range(Demo.size()):
        Demo = Demo.getNext()
        print(Demo.getValue())
        