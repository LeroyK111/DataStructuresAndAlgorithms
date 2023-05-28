#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def __init__(self, solt, data) -> None:
        self.data = data
        self.solt = solt

    def splitTwo(self):
        start = 0
        end = 0
        self.ls = []
        for index, value in enumerate(self.data):
            if index % 2 == 1:
                end = index
                self.ls.append(self.data[start : end + 1])
            else:
                start = index

    def exChange(self):
        for index, value in enumerate(self.ls):
            if index % 2 == 1:
                self.ls[index] = value[::-1]

    def hashTable(self):
        result = sum(map(lambda x: int(x), self.ls))
        remainder = result % len(self.solt)
        self.solt[remainder] = self.data

    def search(self, target):
        self.data = target
        self.splitTwo()
        self.exChange()
        result = sum(map(lambda x: int(x), self.ls))
        remainder = result % len(self.solt)
        # 判断槽位对应内容，是否和target一致。
        if self.solt[remainder] == target:
            return True
        return False

    def run(self):
        # ?拆分折叠
        self.splitTwo()
        # ?隔数反转
        self.exChange()
        # ?hash table
        self.hashTable()

        return self.solt


if __name__ == "__main__":
    data = "12345678"
    solt = [None for _ in range(11)]
    D = Demo(solt=solt, data=data)
    done = D.run()
    print(done)
    done = D.search("1234")
    print(done)
