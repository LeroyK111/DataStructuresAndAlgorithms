#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def __init__(self, **kwargs) -> None:
        self.data = kwargs["data"]
        self.hashTable = kwargs["hashTable"]

    def h(self):
        """
        将数据取余，填入散列表。
        如果存在冲突collision，我们可以使用完美散列函数。
        """
        for i in self.data:
            index = i % len(self.hashTable)
            self.hashTable[index] = i

    def search(self, target):
        index = target % len(self.hashTable)
        if self.hashTable[index] != target:
            return False
        return True

    def run(self):
        self.h()
        """
        槽被数据项占据的比例称为散列表的“负载因子”，这里负载因子为6/11。
        如果要查找某个数据是否存在于表中，我们只需要同一个散列函数，对查找项进行计算，测试返回的槽号所对应的槽中是否有数据项即可。实现了O（1）的复杂度的算法。
        """
        print(self.hashTable)


if __name__ == "__main__":
    data = [56, 26, 93, 17, 31, 77]
    hashTable = [None for _ in range(11)]
    D = Demo(data=data, hashTable=hashTable)
    D.run()
    result = D.search(18)
    print(result)
