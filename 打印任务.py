#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.basic.queue import Queue
import random

"""
打印机。典型队列问题。
"""


class Printer:
    def __init__(self, ppm) -> None:
        # 打印速度
        self.pagerate = ppm
        # 打印任务
        self.currentTask = None
        # 任务倒计时
        self.timeRemaining = 0

    def tick(self):
        # 打印任务
        if self.currentTask is not None:
            # 默认减去一分钟
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        # 打印忙？
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        # 打印新作业
        self.currentTask = newtask
        # 获取这个任务的页数*分钟/打印机页/分钟，获得打印完成时间min
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time) -> None:
        self.timeStamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timeStamp


def newPrintTask():
    """
    模拟需求
    """
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    # numSeconds 总秒
    # pagesPerMinute 页/分钟
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        # 用循环来模拟时间
        if newPrintTask():
            # 一旦有需求，我们就传入启动时间
            task = Task(currentSecond)
            # 将需求放入队尾
            printQueue.enqueue(task)
        
        # 判断打印机是否就绪，并判断队列是否空了
        if not labprinter.busy() and not printQueue.isEmpty():
            # 打印机从队列中取出数据，然后开始打印
            nexttask = printQueue.dequeue()
            # 此时的时间减去任务加入队列的时间
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # 开始执行任务
            labprinter.startNext(nexttask)
        # 标记一下时间
        labprinter.tick()
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("%6.2f, %3d" % (averageWait, printQueue.size()))


for i in range(10):
    simulation(3600, 10)
