#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        # 往队尾放入
        simqueue.enqueue(name)
    print("队列", simqueue.items)

    while simqueue.size() > 1:
        # 小于1就直接弹啊
        for _ in range(num - 1):
            # 队首开始弹五个，再放入五个
            simqueue.enqueue(simqueue.dequeue())
        print("删除前", simqueue.items)
        # 删除第六个
        simqueue.dequeue()
        print("删除后", simqueue.items)
    return simqueue.dequeue()


# 谁是最后热土豆的人
print(hotPotato([1, 2, 3, 4, 5, 6, 7, 8], 6))
