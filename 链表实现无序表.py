#!/usr/bin/python
# -*- coding: utf-8 -*-


class NodeList:
    def __init__(self, item=None) -> None:
        self.head = None
        self.item = item

    def add(self, item):
        # 创建下一个节点
        temp = NodeList(item)
        # 把当前节点head赋值给下一个节点的head
        temp.setNext(self.head)
        # 当前节点head则指向下一个节点的位置
        self.head = temp

    def search(self, item):
        nextNode = self.head
        while nextNode is not None:
            if nextNode.getValue() == item:
                return True
            nextNode = nextNode.getNext()
        return False

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
    # 直接生成链表对象
    Demo = NodeList()

    Demo.add(2)
    Demo.add(3)
    Demo.add(4)
    # two = Demo.getNext()

    # print(two.__dict__)
    # print("链表大小", Demo.size())
    # Demo.remove(3)
    # print(Demo.search(3))
    # print("链表大小", Demo.size())

    # for i in range(Demo.size()):
    #     Demo = Demo.getNext()
    #     result = Demo.getValue()
    #     print(result)

    res = Demo.pop()
    print(res)
