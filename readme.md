 # python数据结构和算法

**2023年4月1日 重温，复习，准备向AI框架进发！**

[早期笔记，有兴趣可以看看](https://github.com/LeroyK111/BasicAlgorithmSet) 什么都有啊，(*^_^*)

本笔记以下列四篇内容为基础，一步一步的归纳自己这些年的开发经验，通过本篇文档展示出来。

https://www.bilibili.com/video/BV1VC4y1x7uv

https://www.youtube.com/watch?v=pkYVOmU3MgA&ab_channel=freeCodeCamp.org

https://zhuanlan.zhihu.com/p/50479555?utm_id=0

https://www.hello-algo.com/

图灵机，模拟器软件。
![](Pasted%20image%2020230402222829.png)

任何一个“**有限能行方法**”下的计算模型可以解决的问题，都算是可计算的。

## 计算机科学

编程是一种通过程序设计语言，将抽象的算法实现为计算机可以执行的代码过程。没有算法，就没有编程。

```math
算法+数据结构=程序
```

程序设计语言需要为算法实现提供实现“过程”和“数据”的机制，具体表现“控制结构”和“数据类型”。

程序设计语言均有语句对应控制结构：顺序处理，分支处理，循环迭代。

数据类型：numeric，non-numeric
![](Pasted%20image%2020230405195035.png)

## 为什么要研究数据结构和算法？

算法研究问题在不同现实的资源约束情况下的不同解决方案，致力于寻找到效率最高的方案。

存在“基于有穷观点的能行方法”的条件下，已被证明不存在解决方案的问题。

利用抽象来保持对问题的”整体感“。

![](Pasted%20image%2020230405195228.png)

数据结构是对ADT的具体实现。（interface是用户直接使用接口）
![](Pasted%20image%2020230405195304.png)
多层次的封装：就是多层次的抽象，让interface越简单越好。
算法具有适用性，合适即可。

## 线性结构Linear Structure

有序数据项目的集合，其中每个数据项目都有唯一的前驱和后继。
第一个数据没有前驱。最后一个数据没有后继。
新的数据加入只会加入到某个数据的前后项目。
这就是线性结构数据。
![](Pasted%20image%2020230409105545.png)

不同线性结构的数据，主要区别是增删改查的使用方式。

### 栈Stack
先入后出，后进先出。数据项的加入和移除都仅仅发生在同一端。
操作端：顶Top
非操作端：底Base
```python
a = [1,2,3,4,5]
# 入栈push
a.append(6)
# 出栈
end = a.pop()
# 窥视栈顶 peek
print(a[-1])
# isempty 检查是否空栈
print("空了") if a == [] else print("非空")
# 数据长度
len(a)
```
不推荐使用起始位，作为操作入口，复杂度为O(N).
### 队列Queue
先入先出，后入后出。新加入的数据项必须在数据集末尾等待，等待时间最长的是队首。
队列中仅有一个入口一个出口，不允许数据项直接插入队中，也不允许从中间移除数据项。
```python
a = []
# 先入
a.insert(0, 5)
# 先出
a.pop()
# 判断空队列
print("空了") if a == [] else print("非空")
# 个数
len(a)
```
### 双端队列Deque
跟队列相似，deque中的数据既可以从队首加入，也可以从队尾加入，数据项可以从两端删除。
```python
a = []
# 队列
a.insert(0, 1)
a.pop()
# 堆栈
a.append()
a.pop()
# 判空
print("空了") if a == [] else print("非空")
# 个数
len(a)
```

### 列表List
没有固定顺序的普通列表。
```python
a=[1,2,3]
# 追加数据
a.append(1)
# 查找数据位置
a.index(1)
# 插入到确定位置
a.insert(0, 1)
# 移除
a.pop(index)
```

#### 采用链表实现无序表。
采用链接节点Node的方式构建数据，需要构建对象传递。
单链表： 每个节点都要维护一个指向next node address
双链表： 每个节点都要维护两个指向previous node address

```python
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

        nextNode = self.head

        while nextNode is not None:

            if nextNode.getValue() == item:

                return True

            nextNode = nextNode.getNext()

        return False

  

    def remove(self, item):

        current = self.head

        prevNode = None

        found = False

  

        """

        快慢指针

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

  
  
  

if __name__ == "__main__":

    # 直接生成链表对象

    Demo = NodeList()

  

    Demo.add(2)

    Demo.add(3)

    Demo.add(4)

    # two = Demo.getNext()

  

    # print(two.__dict__)

    print("链表大小", Demo.size())

    Demo.remove(3)

    # print(Demo.search(3))

    print("链表大小", Demo.size())

    for i in range(Demo.size()):

        Demo = Demo.getNext()

        result = Demo.getValue()

        print(result)


```
#### 链表实现有序表
修改的只有add，search
add 增加遍历，提高了复杂度
search 让遍历难度降低了。
```python
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
```

#### 小结
线性数据结构 Linear DS 以某种 线性次序组织起来。
栈 Stack 维持了数据项后进先出LIFO的次序。
```
stack: push, pop, isEmpty
```

队列Queue维持了数据项先进先出FIFO的次序
```
queue的基本操作包括enqueue，dequeue，isEmpty
```

书写表达式存在前缀prefix，中缀infix，后缀postfix三种。
```
由于栈结构具有次序反转的特性，所以栈结构适合用于开发表达式求值和转换算法。
```

“模拟系统”可以通过一个对现实世界问题的抽象建模，加入随机数，动态运行。为复杂问题的决策提供各种参考情况。
```
队列queue可以用来进行模拟系统的开发。
```

双端队列Deque可以同时具备栈和队列的功能
```
主要操作addfront，addrear，removefront，removerear，isEmpty
```

列表list是数据项能够保持相对位置的数据集
链表的实现，可以保持列表中维持相对位置的特点，而不需要连续的存储空间。但是我们需要对head进行特殊的处理。
```
单链表：值+下一个地址
双链表：上一个地址+值+下一个地址
循环链表：首位地址相连
```

### 递归Recursion
递归是一种解决问题的方法，精髓在于将问题分解为规模更小的**★相同问题**。

可以持续分解，直到问题小到可以用简单直观的计算来解决。

递归的问题分解方式非常独特，其算法方面的明显特征就是：在算法流程中调用自身。

为我们提供了一种复杂问题的优雅解法，精妙的递归算法常会出奇的简单，令人惊叹。

- 递归算法必须有一个基本结束条件。最小规模必须直接解决。
- 递归算法必须能改变状态向基本结束条件演进。
- 递归算法必须调用自身，解决规模减小了的相同问题。

#### 数列求和
```python
def listnum(numlist):
    print(numlist)
    if len(numlist) == 1:
        # 最小规模
        return numlist[0]
    else:
        # 减少规模
        return numlist[0] + listnum(numlist[1:])
print(listnum([1, 2, 3, 4, 5]))
```

#### 进制转换
```python
def toStr(n, base):

    convertString = "0123456789ABCDEF"

    if n < base:

        # 最小规模

        return convertString[n]

    else:

        # 减小规模，调用自身，反向读写数据

        return toStr(n // base, base) + convertString[n % base]

  
  

print(toStr(1453, 16))
```

#### 递归调用为什么类似栈的读写思路?

当一个函数被调用时，系统会把调用时的现场数据压入系统调用栈。
每次调用，压入栈的现场数据称为栈帧。当函数返回时，要从栈顶取得返回地址，恢复现场，弹出栈帧，按地址返回。

![](readme.assets/Pasted%20image%2020230418145808.png)

#### 递归深度限制deep
```python
def tell_store():
	print("从前有座山。。。")
	tell_store()
```
默认递归深度1000，通过递归调用栈计算
```python
import sys
print(sys.getrecursionlimit())

# 设置递归深度
sys.setrecursionlimit(3000)
```

#### 递归可视化
使用一个turtle module内置模块，可视化展现递归。
会打开一个gui然后我们自己画图
```
import turtle
t = turtle.Turtle()
# 开始作图
t.forward(100)

# 结束绘图
turtle.done()
```
画个正方形
```python
for i in range(4):

t.forward(100)

t.right(90)
```
画个五角星
```python
# !五角星

t.pencolor("red")

t.pensize("3")

for i in range(5):

t.forward(100)

t.right(144)

# 隐藏箭头图标

t.hideturtle()
```
递归螺旋
```python
def drawSpiral(t, linelen):

if linelen > 0:

# 最小规模
t.forward(linelen)
t.right(90)

# 递减
drawSpiral(t, linelen - 5)
drawSpiral(t, 100)
```
##### 分形树
自然界中出现的分形特性，使得计算机可以通过分形算法，生成非常逼真的自然场景。
分形就是在不同尺度上都具有相似性的事物。

```python
def tree(branch_len):

if branch_len >= 5:

t.forward(branch_len)

t.right(20)

tree(branch_len - 15)

t.left(40)

tree(branch_len - 15)

t.right(20)

t.backward(branch_len)

  
  

t = turtle.Turtle()

t.left(90)

t.penup()

t.backward(100)

t.pendown()

t.pencolor("green")

t.pensize(2)

tree(70)

t.hideturtle()

turtle.done()
```

![](readme.assets/Pasted%20image%2020230418204857.png)

##### 谢尔宾斯基sierpinski三角形
分形构造，平面称谢尔宾斯基三角形，立体称谢尔宾斯基金字塔。
实际上真正的谢尔宾斯基三角形是完全不可见的，其面积为0，但周长无穷，介于一维和二维之间的分数堆（约1.585维）构造。

```python
def getMid(p1, p2):

return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

  
  

def drawTriangle(points, color):

t.fillcolor(color)

t.penup()

t.goto(points["top"])

t.pendown()

t.goto(points["left"])

t.goto(points["right"])

t.goto(points["top"])

t.end_fill()

  
  

def sierpinski(n, points):

colormap = ["blue", "red", "green", "yellow", "blue", "orange"]

drawTriangle(points, colormap[n])

if n > 0:

sierpinski(n - 1, {"left": points["left"], "top": getMid(points["left"], points["top"]), "right": getMid(points["left"], points["right"])})

  

sierpinski(n - 1, {"left": getMid(points["left"], points["top"]), "top": points["top"], "right": getMid(points["top"], points["right"])})

  

sierpinski(n - 1, {"left": getMid(points["left"], points["right"]), "top": getMid(points["top"], points["right"]), "right": points["right"]})

  
  

points = {"top": (-200, -100), "left": (0, 200), "right": (200, -100)}

sierpinski(5, points)

turtle.done()
```


##### 汉诺塔
```python
count = []

  
  

def moveDisk(disk, fromPole, toPole):

count.append(disk)

print(f"moving disk[{disk}] from {fromPole} to {toPole}")

  
  

def moveTower(height, fromPole, withPole, toPole):

if height >= 1:

moveTower(height - 1, fromPole, toPole, withPole)

moveDisk(height, fromPole, toPole)

moveTower(height - 1, withPole, fromPole, toPole)

  
  

if __name__ == "__main__":

moveTower(5, "#1", "#2", "#3")

print(len(count))
```

##### 探索迷宫（待优化）
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  

from shlex import join

import sys

import turtle as t

import random

import time

"""

使用矩阵创建迷宫.

  

寻找方向避免无限递归的死循环,需要用到面包屑。

  
  

"""

  

sys.set_coroutine_origin_tracking_depth = 100000000000

  
  
  
  

class Maze:

def __init__(self, filePath) -> None:

rowsInMaze = 0

self.mazelist = []

with open(filePath, "r", encoding="utf-8") as f:

for line in f.readlines():

rowList = []

col = 0

for ch in line[:-1]:

# 读取一行中的每列

rowList.append(ch)

  

if ch == "S":

# !找到出发点，记路它的位置

self.startRow = rowsInMaze

self.startCol = col

  

# 列坐标+1

col += 1

# 行坐标+1

rowsInMaze += 1

# 最后将每一行加入到列表中

self.mazelist.append(rowList)

  

def test(self):

print(len(self.mazelist[0]))

print(len(self.mazelist))

print(self.mazelist)

print(self.startRow, self.startCol)

  

def plotMap(self):

t.screensize(1000, 1000, None)

# 设置画笔初始坐标

t.setx(0)

t.sety(0)

# 画笔形状

t.shape("turtle")

t.shapesize(0.5, 0.5)

# 隐藏/展示画笔形状

t.ht()

# t.st()

# 画笔颜色，填充颜色

t.color("black", "orange")

t.speed(0)

  

# 创建墙壁坐标

self.walltTile = []

  

penIndex = [0, 0]

# 开始作画

for row in self.mazelist:

penIndex[0] = 0

t.pu()

t.goto(*penIndex)

t.pd()

for col in row:

if "+" == col:

t.begin_fill()

t.fd(10)

t.right(90)

t.fd(10)

t.right(90)

t.fd(10)

t.right(90)

t.fd(10)

t.right(90)

t.end_fill()

# !将墙砖坐标加入

self.walltTile.append((penIndex[0] + 5, penIndex[1] - 5))

penIndex[0] += 10

t.pu()

t.goto(*penIndex)

t.pd()

penIndex[1] -= 10

  
  
  
  
  
  

def searchPath(self):

# 获取当前朝向

currentHead = t.heading()

# 直接在当前朝向上前进一步

t.fd(10)

# 获取当前位置

currentPosition = tuple(map(lambda x: round(x, 1), t.pos()))

a = random.choice([-1, 1])

# ?判断是否在墙内

if currentPosition in self.walltTile:

# ?在墙内，则后退一步，递归调用本方法

t.bk(10)

t.rt(90 * a)

self.searchPath()

elif currentPosition in self.passing:

t.rt(90 * a)

self.searchPath()

else:

# ?不在墙内，则判断是否在四周墙壁的出口上。

if currentPosition[0] in [5, 255] or currentPosition[1] in [-5, -85]:

# ?在出口,则停止递归，标记自己走来的路

t.fillcolor("red")

self.passing.append(currentPosition)

self.passing.reverse()

self.outletMarker()

else:

# ?不在出口，则递归调用本方法。

if currentPosition not in self.passing:

self.passing.append(currentPosition)

self.searchPath()

def outletMarker(self):

# ?绘制迷宫路径图, 还可以继续优化，消除冗余路径。

for index in self.passing:

t.goto(*index)

t.stamp()

print("Outer Marker")

  

def run(self):

# 画迷宫地图

self.plotMap()

  

# 回到初始位置

t.st()

t.pu()

  

t.home()

self.startRow = self.startRow * -10 - 5

self.startCol = self.startCol * 10 + 5

t.goto(self.startCol, self.startRow)

# 创建已经走过路径数组

self.passing = []

# 记录起始点的位置

self.passing.append(t.pos())

# 计算路径

self.searchPath()

  

t.exitonclick()

  
  

if __name__ == "__main__":

demo = Maze("learning/机器学习/自学算法/DataStructuresAndAlgorithms/maze.txt")

demo.run()

# demo.test()
```
#####  分治策略
将大问题拆解成多个小问题，多个小问题的的解法类同。适合递归的三定律。
![](readme.assets/Pasted%20image%2020230521161546.png)
![](readme.assets/Pasted%20image%2020230521161631.png)

```python
  

def mergeSort(arr):

import math

if (len(arr) < 2):

return arr

# 向下取整

middle = math.floor(len(arr) / 2)

# 列表切割

left, right = arr[0:middle], arr[middle:]

# 调用下一个方法

return merge(mergeSort(left), mergeSort(right))

  
  

def merge(left, right):

result = []

# 当两组列表都存在时

while left and right:

# 各自判断个列表首个元素的大小

if left[0] <= right[0]:

# left弹出这个元素，

result.append(left.pop(0))

else:

# right弹出这个元素

result.append(right.pop(0))

while left:

result.append(left.pop(0))

while right:

result.append(right.pop(0))

return result

  
  

if __name__ == '__main__':

arr = mergeSort(arr=[3, 2, 7, 1])

print(arr)
```

#####  优化问题和贪心策略

![](readme.assets/Pasted%20image%2020230521162057.png)
经典问题找零。
![](readme.assets/Pasted%20image%2020230521162159.png)
Greedy Method
![](readme.assets/Pasted%20image%2020230521162436.png)
贪心策略失效的情况。
![](readme.assets/Pasted%20image%2020230521162745.png)
![](readme.assets/Pasted%20image%2020230521162803.png)
```python

def recMC(coinVaueList, change):

minCoins = change

if change in coinVaueList:

return 1

else:

for i in [c for c in coinVaueList if c <= change]:

print(i)

numCooins = 1 + recMC(coinVaueList, change - i)

if numCooins < minCoins:

minCoins = numCooins

return minCoins

  
  

print(recMC([1, 5, 10, 25], 63))

```
贪心算法优化
![](readme.assets/Pasted%20image%2020230521174409.png)
```python
def recDC(coinVaueList, change, knownResults):

minCoins = change

if change in coinVaueList:

# 递归最优解，记录

knownResults[change] = 1

return 1

elif knownResults[change] > 0:

return knownResults[change]

else:

for i in [c for c in coinVaueList if c <= change]:

numCoins = 1 + recDC(coinVaueList, change - i, knownResults)

if numCoins < minCoins:

minCoins = numCoins

knownResults[change] = minCoins

  

return minCoins
```

##### 动态规划
每一步都和前一步的结果有关。
```python
  

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):

# 从1分开始到change，逐个计算最少的硬币数

for cents in range(1, change + 1):

# 初始化一个最大值

coinCount = cents

newCoin = 1

# 减去每个硬币，向后查最少硬币数，同时记录总的最少数

for j in [c for c in coinValueList if c <= cents]:

if minCoins[cents - j] + 1 < coinCount:

coinCount = minCoins[cents - j] + 1

newCoin = j

# 得到最少的硬币数，记录到表中

minCoins[cents] = coinCount

# 记录本步骤加的一个硬币

coinsUsed[cents] = newCoin

  

# 返回最后一个结果

return minCoins[change]

  
  

def printCoins(coinsUsed, change):

coin = change

while coin > 0:

thisCoin = coinsUsed[coin]

print(thisCoin)

coin = coin - thisCoin

  
  

if __name__ == "__main__":

amnt = 63

clist = [1, 5, 10, 21, 25]

coinsUsed = [0] * (amnt + 1)

coinCount = [0] * (amnt + 1)

dpMakeChange(clist, amnt, coinCount, coinsUsed)

printCoins(coinsUsed, amnt)

# print(coinsUsed)
```

博物馆大盗问题。
![](readme.assets/Pasted%20image%2020230521183325.png)
![](readme.assets/Pasted%20image%2020230521183308.png)

```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  

# 博物馆宝物价值

tr = [None, {"w": 2, "v": 3}, {"w": 3, "v": 4}, {"w": 4, "v": 8}, {"w": 5, "v": 8}, {"w": 9, "v": 10}]

  
  

# 大盗最大承重20

max_w = 20

  

# 初始化二维表格m[(i, w)]

# 表示前i个宝物中，最大重量w的组合，所得到的最大价值

# 当i什么都不取，或w上线为0，则价值为0

m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

  

# print(m)

  

# 逐个填写二维表格

for i in range(1, len(tr)):

for w in range(1, max_w + 1):

# !遍历全部表格

if tr[i]["w"] > w:

# 如果装不下第i个宝物，那就不装

m[(i, w)] = m[(i - 1, w)]

else:

m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]["w"])] + tr[i]["w"])

  
  

if __name__ == "__main__":

result = m[(len(tr) - 1, max_w)]

print(result)
```
#### 小结
**递归算法和动态规划，其实可以相互转换的。**
![](readme.assets/Pasted%20image%2020230521201308.png)

### 排序查找算法

#### 顺序查找算法 sequential search
线性阶O(n)，算法。
```python
def sequentialSearch(alist, item):

pos = 0

found = False

  

while pos < len(alist) and not found:

if alist[pos] == item:

found = True

  

else:

pos += 1

  

return found

  
  

if __name__ == "__main__":

testList = [1, 2, 32, 8]

print(sequentialSearch(testList, 32))
```

#### 二分查找算法binarySearch
只能针对有序表。无序表还需要考虑排序的开销。
对数阶O(log n)，算法。
```python

def binarySearch(alist, item):

first = 0

last = len(alist) - 1

found = False

  

while first <= last and not found:

midPoint = (first + last) // 2

if alist[midPoint] == item:

found = True

else:

if item < alist[midPoint]:

last = midPoint - 1

else:

first = midPoint + 1

  

return found

  
  

if __name__ == "__main__":

testlist = [1, 2, 3, 5]

print(binarySearch(testlist, 2))
```

#### 冒泡排序Bubble Sort
平方阶O(n^2)，算法。
```python

def bubbleSort(alist):

exchanges = True

  

for passnum in range(len(alist) - 1, 0, -1):

for i in range(passnum):

if alist[i] > alist[i + 1]:

alist[i], alist[i + 1] = alist[i + 1], alist[i]

  
  

def shortBubbleSort(alist):

exchanges = True

passnum = len(alist) - 1

while passnum > 0 and exchanges:

exchanges = False

for i in range(passnum):

if alist[i] > alist[i + 1]:

exchanges = True

alist[i], alist[i + 1] = alist[i + 1], alist[i]

  

passnum = passnum - 1

  
  

if __name__ == "__main__":

alist = [54, 26, 25, 17, 56, 78]

# bubbleSort(alist)

shortBubbleSort(alist)

print(alist)
```


#### 选择排序 selection sort
索引交换，比冒泡稍好一些。 
平方阶O(n^2)，算法。
```python
  

def selectionSort(alist):

for fillslot in range(len(alist) - 1, 0, -1):

positionOfMax = 0

for location in range(1, fillslot + 1):

if alist[location] > alist[positionOfMax]:

positionOfMax = location

  

temp = alist[fillslot]

alist[fillslot] = alist[positionOfMax]

alist[positionOfMax] = temp

  
  

if __name__ == "__main__":

alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]

selectionSort(alist)

print(alist)
```


#### 插入排序 insertion sort
平方阶O(n^2)，算法。
```python
def insertionSort(alist):

for index in range(1, len(alist)):

currentValue = alist[index]

position = index

  

while position > 0 and alist[position - 1] > currentValue:

alist[position] = alist[position - 1]

position = position - 1

  

alist[position] = currentValue

  
  

if __name__ == "__main__":

alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]

insertionSort(alist)

print(alist)
```
#### 谢尔排序 shell sort
比插入排序要好一些。
平方阶O(n)，算法。
```python
def shellSort(alist):

subListCount = len(alist) // 2

while subListCount > 0:

for startPosition in range(subListCount):

gapInsertionSort(alist, startPosition, subListCount)

  

subListCount = subListCount // 2

  
  

def gapInsertionSort(alist, startPosition, subListCount):

for i in range(startPosition + subListCount, len(alist), subListCount):

currentValue = alist[i]

position = i

while position >= subListCount and alist[position - subListCount] > currentValue:

alist[position] = alist[position - subListCount]

position = position - subListCount

  

alist[position] = currentValue

  
  
  

if __name__ == '__main__':

alist = [2, 3, 14, 1, 51234, 5, 36, 45267, 12]

shellSort(alist)

print(alist)
```
#### 归并排序 merge sort
归并排序，递归。 用空间换时间。
对数阶O(log n) 算法。
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

def mergeSort(alist):

if len(alist) > 1:

mid = len(alist) // 2

leftHalf = alist[:mid]

rightHalf = alist[mid:]

  

mergeSort(leftHalf)

mergeSort(rightHalf)

  

i = j = k = 0

  

while i < len(leftHalf) and j < len(rightHalf):

if leftHalf[i] < rightHalf[j]:

alist[k] = leftHalf[i]

i += 1

else:

alist[k] = rightHalf[j]

j += 1

  

k += 1

  

while i < len(leftHalf):

alist[k] = leftHalf[i]

i += 1

k += 1

  

while j < len(rightHalf):

alist[k] = rightHalf[j]

j += 1

k += 1

  
  

def merge_sort(lst):

if len(lst) <= 1:

return lst

  

middle = len(lst) // 2

left = merge_sort(lst[:middle])

right = merge_sort(lst[middle:])

  

merged = []

while left and right:

if left[0] <= right[0]:

merged.append(left.pop(0))

else:

merged.append(right.pop(0))

merged.extend(right if right else left)

  

return merged

  
  

if __name__ == "__main__":

alist = [2, 3, 1, 41, 24, 151, 2345, 3456, 234, 12345, 123, 32, 34]

# mergeSort(alist)

# print(alist)

  

print(merge_sort(alist))
```
#### 快速排序quick sort
归并排序，递归。 用空间换时间。
对数阶O(log n) 算法。

```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

def quickSort(alist):

quickSortHelper(alist, 0, len(alist) - 1)

  
  

def partition(alist, first, last):

# 选定中值

pivotValue = alist[first]

  

# 左右标初值

leftMark = first + 1

rightMark = last

  

done = False

  

while not done:

# 向右移动左标

while leftMark <= rightMark and alist[leftMark] <= pivotValue:

leftMark += 1

  

# 向左移动右标

while alist[rightMark] >= pivotValue and rightMark >= leftMark:

rightMark -= 1

  

# 两标相错，结束移动

if rightMark < leftMark:

done = True

else:

# 左右标的值交换

alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

  

# 中间值就位

alist[first], alist[rightMark] = alist[rightMark], alist[first]

  

# 中间值点，分裂点

return rightMark

  
  

def quickSortHelper(alist, first, last):

# 基本结束条件

if first < last:

# 分裂

splitPoint = partition(alist, first, last)

# 递归调用

quickSortHelper(alist, first, splitPoint - 1)

quickSortHelper(alist, splitPoint + 1, last)

  
  

if __name__ == "__main__":

alist = [54, 26, 25, 17, 56, 78]

# bubbleSort(alist)

quickSort(alist)

print(alist)
```

### 散列Hashing

如果数据项之间是按照大小排序，就可以使用二分查找来降低算法复杂度。
但是如果我们进一步构造一个数据结构，使得查找算法降低O(1), 这种概念被称为“散列”。

散列表：hash table，是一种数据集，快速查找定位。每一个存储位置称为槽（slot），可用来保存数据项，每个槽具有唯一的名称。
实现数据项到存储槽名称转换的，称为散列函数（hash function）。
```python
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
```

#### 完美散列函数
典型的拿空间换时间。
![](readme.assets/Pasted%20image%2020230528162405.png)
再怎么散列数据，也会出现槽位不够用的情况。形成1对1映射情况。
![](readme.assets/Pasted%20image%2020230528163107.png)
作为一致性校验的数据指纹函数，需要具备如下特性。
![](readme.assets/Pasted%20image%2020230528164106.png)
#### 近似完美散列
##### MD5
md5函数：可以将任何长度的数据变换成为固定长度为128bit的摘要。
##### SHA
sha-0/sha-1 输出散列值160bit。
sha-256/sha-224 分别输出散列值256bit，224bit。
sha-512/sha-384 分别输出散列值512bit，384bit。
```python
import hashlib as hs

  
  

def md5(str):

return hs.md5(str).hexdigest()

  
  

def sha1(str):

return hs.sha1(str).hexdigest()

  
  

def md5Step(str):

m = hs.md5()

m.update(str)

  

return m.hexdigest()

  
  

if __name__ == "__main__":

message = "Hello, world!".encode("utf-8")

print(message)

print(md5(message))

print(sha1(message))

print(md5Step(message))
```
#### 其他用处
![](readme.assets/Pasted%20image%2020230528170227.png)
![](readme.assets/Pasted%20image%2020230528170326.png)
![](readme.assets/Pasted%20image%2020230528170352.png)

#### 区块链技术
本质：分布式数据库
![](readme.assets/Pasted%20image%2020230528170858.png)
![](readme.assets/Pasted%20image%2020230528170956.png)
![](readme.assets/Pasted%20image%2020230528171232.png)
##### 为什么区块链技术不具有伪造性？
![](readme.assets/Pasted%20image%2020230528171300.png)
![](readme.assets/Pasted%20image%2020230528171452.png)
![](readme.assets/Pasted%20image%2020230528171649.png)
散列值无法逆向。
![](readme.assets/Pasted%20image%2020230528171752.png)
bitcoin比特币中的一个区块。
![](readme.assets/Pasted%20image%2020230528171934.png)
![](readme.assets/Pasted%20image%2020230528172050.png)
维持方式：
![](readme.assets/Pasted%20image%2020230528172157.png)
#### 散列函数的设计
##### 折叠法
```python
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

# 拆分折叠

self.splitTwo()

# 隔数反转

self.exChange()

# hash table

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
```
##### 平方取中法
```python
def middleSquareMethod(data, slot):

data = str(data**2)

middleEnd = len(data) // 2

middleStart = middleEnd - 1

result = int(data[middleStart] + data[middleEnd])

# 开始进行散列函数

index = result % len(slot)

slot[index] = data

return slot

  
  

if __name__ == "__main__":

data = 44

slot = [None for _ in range(11)]

result = middleSquareMethod(data, slot)

print(result)
```
##### 非数项
字符串ascii转换。
```python
def hashStr(data, slot):

result = []

for i in data:

result.append(ord(i))

done = sum(result)

# 开始散列

index = done % len(slot)

slot[index] = data

  

return slot

  
  

if __name__ == "__main__":

data = "asdsdaf"

slot = [None for i in range(11)]

print(hashStr(data, slot))
```
基本出发点，散列函数不能成为存储和查找过程的计算负载。

##### 冲突解决方案
得想个办法，解决多对一的问题。
![](readme.assets/Pasted%20image%2020230528215502.png)
##### 开放定址
![](readme.assets/Pasted%20image%2020230528215720.png)
###### 线性探测
![](readme.assets/Pasted%20image%2020230528215845.png)
###### 跳跃式探测
![](readme.assets/Pasted%20image%2020230528215955.png)
###### 再散列
散列表的大小建议为素数。
![](readme.assets/Pasted%20image%2020230528220110.png)
###### 二次探测
![](readme.assets/Pasted%20image%2020230528220209.png)
###### 数据项链
![](readme.assets/Pasted%20image%2020230528220252.png)

#### 映射抽象数据类型
手动创建映射map类型。
![](readme.assets/Pasted%20image%2020230528220557.png)

```python


#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

class HashTable(object):

def __init__(self) -> None:

self.size = 11

self.slots = [None] * self.size

self.data = [None] * self.size

  

def hashfunction(self, key):

return key % self.size

  

def rehash(self, oldHash):

return (oldHash + 1) % self.size

  

def put(self, key, data):

hashvalue = self.hashfunction(key)

  

if self.slots[hashvalue] is None:

self.slots[hashvalue] = key

self.data[hashvalue] = data

else:

if self.slots[hashvalue] == key:

self.data[hashvalue] = data

else:

nextslot = self.rehash(hashvalue)

while self.slots[nextslot] is not None and self.slots[nextslot] != key:

nextslot = self.rehash(nextslot)

if self.slots[nextslot] is not None:

self.slots[nextslot] = key

self.data[nextslot] = data

else:

self.data[nextslot] = data

  

def get(self, key):

startslot = self.hashfunction(key)

data = None

stop = False

found = False

position = startslot.find

  

while self.slots[position] is not None and not found and not stop:

if self.slots[position] == key:

found = True

data = self.data[position]

else:

position = self.rehash(position)

if position == startslot:

stop = True

return data

  

def __getitem__(self, key):

return self.get(key)

  

def __setitem__(self, key, data):

self.put(key, data)
```
![](readme.assets/Pasted%20image%2020230528223622.png)
![](readme.assets/Pasted%20image%2020230528223659.png)
### 树Tree
**基本的非线性的数据结构：树。
分为基本三部分：根root，枝branch，叶leaf
特点：层次化，独立隔离，唯一。**
![](readme.assets/Pasted%20image%2020230528230007.png)
![](readme.assets/Pasted%20image%2020230528230037.png)
![](readme.assets/Pasted%20image%2020230528230059.png)
![](readme.assets/Pasted%20image%2020230528230119.png)
#### 举例
![](readme.assets/Pasted%20image%2020230528230220.png)
![](readme.assets/Pasted%20image%2020230528230248.png)
#### 名词解释
节点Node：组成树的基本部分。
每个节点具有名称，或“键值”，节点还可以保存额外数据项，根据不同的应用而变。

边Edge: 边是组成树的另一个部分
每条边恰好连接两个节点，表示节点之间具有关联，边具有出入方向。
每个节点（除根节点外）恰有一条来自另一节点的入边。
每个节点可以有多条连到其他节点的出边。

根root：数中唯一没有入边的节点。

路径Path：由边依次连接在一起的节点的有序列表。

![](readme.assets/Pasted%20image%2020230601003703.png)
子节点children：入边均来自同一个节点的若干节点，称为这个节点的子节点。
父节点Parent:  一个节点是其他所有出边的连接节点的父节点。
![](readme.assets/Pasted%20image%2020230601003928.png)
兄弟节点Sibling: 具有同一个父节点的节点之间称为兄弟节点。
子树Subtree：一个节点和其他所有子孙节点，以及相关边的集合。
![](readme.assets/Pasted%20image%2020230601004600.png)
叶节点Leaf：没有子节点的节点称为叶节点。
层级Level：从根节点开始到达一个节点的路径，所包含的边数量，称为这个节点的层级。
高度：树中所有节点的最大层级称为树的高度。
![](readme.assets/Pasted%20image%2020230601004755.png)
##### 树的定义1——连接定义
![](readme.assets/Pasted%20image%2020230601004956.png)
##### 树的定义2——递归定义
![](readme.assets/Pasted%20image%2020230601005104.png)
##### 嵌套列表法
![](readme.assets/Pasted%20image%2020230601005749.png)
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

"""

! 使用列表[root, left, right]嵌套实现二叉树

"""

  

myTree = ["a", ["b", ["d"], ["e"]], ["c", ["f"]]]

  
  

def BinaryTree(r):

return [r, [], []]

  
  

def insertLeft(root, newBranch):

t = root.pop()

if len(t) > 1:

root.insert(1, [newBranch, t, []])

else:

root.insert(1, [newBranch, t, [], []])

  

return root

  
  

def insertRight(root, newBranch):

t = root.pop()

if len(t) > 1:

root.insert(2, [newBranch, [], t])

else:

root.insert(2, [newBranch, [], []])

return root

  
  

def getRootVal(root):

return root[0]

  
  

def setRootVal(root, newVal):

root[0] = newVal

  
  

def getLeftChild(root):

return root[1]

  
  

def getRightChild(root):

return root[2]

  
  

if __name__ == "__main__":

# print(myTree)

  

r = BinaryTree(3)

insertLeft(r, 4)

insertLeft(r, 5)

insertRight(r, 6)

insertRight(r, 7)

ls = getLeftChild(r)

print(ls)

  

setRootVal(ls, 9)

print(r)

  

insertLeft(ls, 11)

print(r)

print(getRightChild(getRightChild(r)))
```
##### 节点链接法
**本质就是对象的嵌套，每个对象都存储了两个地址，一个自身值**
![](readme.assets/Pasted%20image%2020230601014459.png)
```python
"""

生成二叉树

"""

  
  

class Node(object):

def __init__(self, data):

self.left = None # 左节点

self.right = None # 右节点

self.data = data # 值

  

def insert(self, data):

if data is None:

# 让-999替代none

data = -999

  

# 将新值与父节点进行比较

if self.data: # 非空

if data <= self.data: # !新值较小，放左边，考虑到none值的存在，所以小于等于，不然直接小于就行

if self.left is None: # 若空，则新建插入节点

# !新建一个对象，传入当前根节点的左节点对象，

self.left = Node(data)

else: # !否则，递归调用对象的方法，往下查找，

self.left.insert(data)

elif data > self.data: # 新值较大，放右边

if self.right is None: # 若空，则新建插入对象

self.right = Node(data)

else: # 否则，递归往下查找

self.right.insert(data)

else:

# 空值则只有起始对象

self.data = data

  

def PrintTree(self):

# 这里使用的还是中序遍历

if self.left:

self.left.PrintTree()

print(self.data)

if self.right:

self.right.PrintTree()

  

def fil(self, data: list):

return list(map(lambda x: None if x == -999 else x, data))

  

# 中序遍历

# Left -> Root -> Right

def inorderTraversal(self, root):

res = []

if root:

# 先查找左节点

res = self.inorderTraversal(root.left)

# 加入根节点

res.append(root.data)

# 开始查找右节点

res = res + self.inorderTraversal(root.right)

return self.fil(res)

  

# 先序遍历

# Root -> Left ->Right

def PreorderTraversal(self, root):

res = []

if root:

res.append(root.data)

res = res + self.PreorderTraversal(root.left)

res = res + self.PreorderTraversal(root.right)

return self.fil(res)

  

# 后序遍历

# Left ->Right -> Root

def PostorderTraversal(self, root):

res = []

if root:

res = self.PostorderTraversal(root.left)

res = res + self.PostorderTraversal(root.right)

res.append(root.data)

return self.fil(res)

  
  

if __name__ == "__main__":

# 创建节点

root = Node(12)

# 插入节点

root.insert(6)

root.insert(14)

root.insert(3)

  

# 打印所有的树

# root.PrintTree()

  

# 中序遍历 [3, 6, 12, 14]

result = root.inorderTraversal(root)

print(result)

# 先序遍历 [12, 6, 3, 14]

result = root.PreorderTraversal(root)

print(result)

# 后续遍历 [3, 6, 14, 12]

result = root.PostorderTraversal(root)

print(result)
```
##### 树的解析——语法树
![](readme.assets/Pasted%20image%2020230601015655.png)
![](readme.assets/Pasted%20image%2020230601015738.png)
![](readme.assets/Pasted%20image%2020230601015812.png)
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

from pythonds.basic.stack import Stack

from pythonds.trees.binaryTree import BinaryTree

  

import operator

  
  

def buildParseTree(fpexp):

fplist = fpexp

pStack = Stack()

eTree = BinaryTree("")

# 入栈下降

pStack.push(eTree)

currentTree = eTree

for i in fplist:

# 表达式开始

if i == "(":

currentTree.insertLeft("")

# 入栈下降

pStack.push(currentTree)

currentTree = currentTree.getLeftChild()

elif i not in ["+", "-", "*", "/", ")"]:

# 操作数

currentTree.setRootVal(int(i))

# 出栈上升

parent = pStack.pop()

currentTree = parent

elif i in ["+", "*", "/", "-"]:

# 操作符

currentTree.setRootVal(i)

currentTree.insertRight("")

pStack.push(currentTree)

currentTree = currentTree.getRightChild()

elif i == ")":

# 出栈上升

currentTree = pStack.pop()

else:

raise ValueError

return eTree

  
  

def evaluate(paresTree):

# 递归求解

opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

  

leftC = paresTree.getLeftChild()

rightC = paresTree.getRightChild()

  

if leftC and rightC:

fn = opers[paresTree.getRootVal()]

return fn(evaluate(leftC), evaluate(rightC))

else:

return paresTree.getRootVal()

  
  
  

if __name__ == "__main__":

expression = ["(", "3", "+", "(", "4", "*", "5", ")", ")"]

result = buildParseTree(expression)

# print(result)

# print(result.getRootVal(), result.getLeftChild().key)

result = evaluate(result)

print(result)
```
##### 树的遍历
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

def preorder(tree):

# 前序遍历

if tree:

print(tree.getRootVal())

preorder(tree.getLeftChild())

preorder(tree.getRightChild())

  
  

def postorder(tree):

# 中序遍历

if tree is not None:

postorder(tree.getLeftChild())

postorder(tree.getRightChild())

print(tree.getRootVal())

  
  

def inorder(tree):

# 后续遍历

if tree is not None:

inorder(tree.getLeftChild())

print(tree.getRootVal())

inorder(tree.getRightChild())
```
##### 优先队列和二叉堆
队列本身是先进先出FIFO数据结构。
但是存在一种队列变体称为“优先队列”，在系统进程调度中某些重要进程可以插入到队列最前。
思路：出栈还是pop，但是入栈需要根据value的优先级，插队进入 到 某个index 上。

方法：
优先队列的经典方案是采用二叉堆数据结构，能够将入队和出队复杂度都保持在O(log n)
二叉堆的有趣之处在于其逻辑上似二叉树，却是用非嵌套的列表来实现的。
最小key排在队首，称为 “最小堆minheap”。反之，最大key排在队首的是”最大堆max heap“

![](readme.assets/Pasted%20image%2020230704222926.png)
满二叉树，平衡二叉树、是最理想的情况。

但是往往都是由完全二叉树进行 叶节点 的生成。

通过无序表做列表实现。
![](readme.assets/Pasted%20image%2020230704223123.png)
堆次序。
![](readme.assets/Pasted%20image%2020230704223521.png)

优先队列的实现
```python
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



```

##### 二叉堆的实现
```python
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
```
##### 二叉查找树
Binary Search  Tree

有序表数据结构+二分搜索算法
散列表数据结构+散列及冲突解决算法

核心：
二叉树数据结构+二叉树搜索算法
![](readme.assets/Pasted%20image%2020230705005335.png)
![](readme.assets/Pasted%20image%2020230705005419.png)

BST & TreeNode
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

class TreeNode:

def __init__(self, key, val, left=None, right=None, parent=None) -> None:

self.key = key

self.payload = val

self.leftChild = left

self.rightChild = right

self.parent = parent

  

def hasLeftChild(self):

return self.leftChild

  

def hasRightChild(self):

return self.rightChild

  

def isLeftChild(self):

return self.parent and self.parent.leftChild == self

  

def isRightChild(self):

return self.parent and self.parent.rightChild == self

  

def isRoot(self):

return not self.parent

  

def isLeaf(self):

return not (self.rightChild or self.leftChild)

  

def hasAnyChildren(self):

return self.rightChild or self.leftChild

  

def hasBothChildren(self):

return self.rightChild and self.leftChild

  

def replaceNodeData(self, key, value, lc, rc):

self.key = key

self.payload = value

self.leftChild = lc

self.rightChild = rc

  

if self.hasLeftChild():

self.leftChild.parent = self

if self.hasRightChild():

self.rightChild.parent = self

  

def __iter__(self):

# 迭代器

if self:

if self.hasLeftChild():

for elem in self.leftChild:

yield elem

yield self.key

if self.hasRightChild():

for elem in self.rightChild:

yield elem

  

def findSuccessor(self):

succ = None

if self.hasRightChild():

succ = self.rightChild.findMin()

else:

if self.parent:

if self.isLeftChild():

succ = self.parent

else:

self.parent.rightChild = None

succ = self.parent.findSuccessor()

self.parent.rightChild = self

return succ

  

def findMin(self):

current = self

while current.hasLeftChild():

current = current.leftChild

return current

  

def spliceOut(self):

if self.isLeaf():

if self.isLeftChild():

self.parent.leftChild = None

else:

self.parent.rightChild = None

elif self.hasAnyChildren():

if self.hasLeftChild():

if self.isLeftChild():

self.parent.leftChind = self.leftChild

else:

self.parent.rightChind = self.leftChild

self.leftChild.parent = self.parent

else:

if self.isLeftChild():

self.parent.leftChind = self.rightChild

else:

self.parent.rightChind = self.rightChild

self.rightChild.parent = self.parent

  
  

class BinarySearchTree:

# 构造b树

def __init__(self) -> None:

self.root = None

self.size = 0

  

def length(self):

return self.size

  

def __len__(self):

return self.size

  

def __iter__(self):

return self.root.__iter__()

  

def put(self, key, val):

if self.root:

self._put(key, val, self.root)

else:

self.root = TreeNode(key, val)

self.size += 1

  

def _put(self, key, val, currentNode):

# 插入子树

if key < currentNode.key:

# 左子树

if currentNode.hasLeftChild():

self._put(key, val, currentNode.leftChild)

else:

currentNode.leftChild = TreeNode(key, val, parent=currentNode)

else:

if currentNode.hasRightChild():

# 右子树

self._put(key, val, currentNode.rightChild)

else:

currentNode.rightChild = TreeNode(key, val, parent=currentNode)

  

def __setitem__(self, k, v):

# 拦截字典传参数

self.put(k, v)

  

def get(self, key):

if self.root:

res = self._get(key, self.root)

if res:

return res.payload

else:

return None

else:

return None

  

def _get(self, key, currentNode):

if not currentNode:

return None

elif currentNode.key == key:

return currentNode

elif key < currentNode.key:

return self._get(key, currentNode.leftChild)

else:

return self._get(key, currentNode.rightChild)

  

def __getitem__(self, key):

return self.get(key)

  

def __contains__(self, key):

if self._get(key, self.root):

return True

else:

return False

  

def remove(self, currentNode):

if currentNode.isLeaf():

# 没有子节点的方法，直接删除

if currentNode == currentNode.parent.leftChild:

currentNode.parent.leftChild = None

else:

currentNode.parent.rightChild = None

elif currentNode.hasBothChildren():

succ = currentNode.findSuccessor()

succ.spliceOut()

currentNode.key = succ.key

currentNode.payload = succ.payload

else:

if currentNode.hasLeftChild():

if currentNode.isLeftChild():

# 左子节点删除

currentNode.leftChild.parent = currentNode.parent

currentNode.parent.leftChild = currentNode.leftChild

elif currentNode.isRightChild():

# 右子节点删除

currentNode.leftChild.parent = currentNode.parent

currentNode.parent.rightChild = currentNode.rightChild

else:

# 根节点删除

currentNode.replaceNodeData(

currentNode.leftChild,

currentNode.leftChild.payload,

currentNode.leftChild.leftChild,

currentNode.leftChild.rightChild,

)

else:

if currentNode.isLeftChild():

# 左子节点删除

currentNode.rightChild.parent = currentNode.parent

currentNode.parent.leftChild = currentNode.leftChild

elif currentNode.isRightChild():

# 右子节点

currentNode.rightChild.parent = currentNode.parent

currentNode.parent.rightChild = currentNode.rightChild

else:

# 根节点删除

currentNode.replaceNodeData(

currentNode.rightChild,

currentNode.rightChild.payload,

currentNode.rightChild.leftChild,

currentNode.rightChild.rightChild,

)

  

def delete(self, key):

if self.size > 1:

nodeToRemove = self._get(key, self.root)

if nodeToRemove:

self.remove(nodeToRemove)

self.size -= 1

else:

raise KeyError("nof found key")

  

elif self.size == 1 and self.root.key == key:

self.root = None

self.size -= 1

else:

raise KeyError("not found key")

  

def __delitem__(self, key):

self.delete(key)

  
  

if __name__ == "__main__":

myTree = BinarySearchTree()

# 字典传参数

myTree[3] = "red"

myTree[4] = "blue"

myTree[6] = "yellow"

myTree[2] = "at"

  

# 归属判断

print(3 in myTree)

# 索引

print(myTree[6])

  

# 删除

del myTree[3]

  

# 循环

for key in myTree:

print(key, myTree[key])
```

##### AVL树的定义和性能
与上一个完全二叉树不同，这里是平衡二叉树。
![](readme.assets/Pasted%20image%2020230708222604.png)
![](readme.assets/Pasted%20image%2020230708222738.png)
![](readme.assets/Pasted%20image%2020230708223353.png)
AVL平衡树可以保持BST树的性能，避免退化的情形。
从子节点的不平衡性，会往父节点一直传递，直到根节点为止。
但是当某一层父节点恢复到平衡因子为0时，则该层往上不会继续传递不平衡性。
某个层级的节点更改，不会影响上层的平衡因子。

```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

class TreeNode:

def __init__(self, key, val, left=None, right=None, parent=None) -> None:

self.key = key

self.payload = val

self.leftChild = left

self.rightChild = right

self.parent = parent

  

def hasLeftChild(self):

return self.leftChild

  

def hasRightChild(self):

return self.rightChild

  

def isLeftChild(self):

return self.parent and self.parent.leftChild == self

  

def isRightChild(self):

return self.parent and self.parent.rightChild == self

  

def isRoot(self):

return not self.parent

  

def isLeaf(self):

return not (self.rightChild or self.leftChild)

  

def hasAnyChildren(self):

return self.rightChild or self.leftChild

  

def hasBothChildren(self):

return self.rightChild and self.leftChild

  

def replaceNodeData(self, key, value, lc, rc):

self.key = key

self.payload = value

self.leftChild = lc

self.rightChild = rc

  

if self.hasLeftChild():

self.leftChild.parent = self

if self.hasRightChild():

self.rightChild.parent = self

  

def __iter__(self):

# 迭代器

if self:

if self.hasLeftChild():

for elem in self.leftChild:

yield elem

yield self.key

if self.hasRightChild():

for elem in self.rightChild:

yield elem

  

def findSuccessor(self):

succ = None

if self.hasRightChild():

succ = self.rightChild.findMin()

else:

if self.parent:

if self.isLeftChild():

succ = self.parent

else:

self.parent.rightChild = None

succ = self.parent.findSuccessor()

self.parent.rightChild = self

return succ

  

def findMin(self):

current = self

while current.hasLeftChild():

current = current.leftChild

return current

  

def spliceOut(self):

if self.isLeaf():

if self.isLeftChild():

self.parent.leftChild = None

else:

self.parent.rightChild = None

elif self.hasAnyChildren():

if self.hasLeftChild():

if self.isLeftChild():

self.parent.leftChind = self.leftChild

else:

self.parent.rightChind = self.leftChild

self.leftChild.parent = self.parent

else:

if self.isLeftChild():

self.parent.leftChind = self.rightChild

else:

self.parent.rightChind = self.rightChild

self.rightChild.parent = self.parent

  
  

class BinarySearchTree:

# 构造b树

def __init__(self) -> None:

self.root = None

self.size = 0

  

def length(self):

return self.size

  

def __len__(self):

return self.size

  

def __iter__(self):

return self.root.__iter__()

  

def put(self, key, val):

if self.root:

self._put(key, val, self.root)

else:

self.root = TreeNode(key, val)

self.size += 1

  

# 调整因子

def updateBalance(self, node):

if node.balanceFactor > 1 or node.balanceFactor < -1:

# 重新平衡函数

self.rebalance(node)

return

if node.parent is not None:

if node.isLeftChild():

node.parent.balanceFactor += 1

elif node.isRightChild():

node.parent.balanceFactor -= 1

if node.parent.balanceFactor != 0:

# 调整父节点因子

self.updateBalance(node.parent)

  

def rebalance(self, node):

# 再平衡

if node.balanceFactor < 0:

# 右重需要右旋

if node.rightChild.balanceFactor > 0:

self.rotateRight(node.rightChild)

self.rotateLeft(node)

else:

self.rotateLeft(node)

elif node.balanceFactor > 0:

if node.leftChild.balanceFactor < 0:

self.rotateLeft(node.leftChild)

self.rotateRight(node)

else:

self.rotateRight(node)

  

def rotateLeft(self, rotRoot):

newRoot = rotRoot.rightChild

rotRoot.rightChild = newRoot.leftChild

if newRoot.leftChild is not None:

newRoot.leftChild.parent = rotRoot

newRoot.parent = newRoot.parent

if rotRoot.isRoot():

self.root = newRoot

else:

if rotRoot.isLeftChild():

rotRoot.parent.leftChild = newRoot

else:

rotRoot.parent.rightChild = newRoot

newRoot.leftchild = rotRoot

rotRoot.parent = newRoot

rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)

newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

  

def rotateRight(self, rotRoot):

newRoot = rotRoot.leftChild

rotRoot.leftChild = newRoot.rightChild

if newRoot.rightChild is not None:

newRoot.rightChild.parent = rotRoot

newRoot.parent = newRoot.parent

if rotRoot.isRoot():

self.root = newRoot

else:

if rotRoot.isRightChild():

rotRoot.parent.rightChild = newRoot

else:

rotRoot.parent.leftChild = newRoot

newRoot.rightChild = rotRoot

rotRoot.parent = newRoot

rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)

newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

  

def _put(self, key, val, currentNode):

if key < currentNode.key:

# 左子树

if currentNode.hasLeftChild():

self._put(key, val, currentNode.leftChild)

else:

currentNode.leftChild = TreeNode(key, val, parent=currentNode)

# 增加调整因子

self.updateBalance(currentNode.leftChild)

else:

if currentNode.hasRightChild():

# 右子树

self._put(key, val, currentNode.rightChild)

else:

currentNode.rightChild = TreeNode(key, val, parent=currentNode)

self.updateBalance(currentNode.rightClild)

  

def __setitem__(self, k, v):

# 拦截字典传参数

self.put(k, v)

  

def get(self, key):

if self.root:

res = self._get(key, self.root)

if res:

return res.payload

else:

return None

else:

return None

  

def _get(self, key, currentNode):

if not currentNode:

return None

elif currentNode.key == key:

return currentNode

elif key < currentNode.key:

return self._get(key, currentNode.leftChild)

else:

return self._get(key, currentNode.rightChild)

  

def __getitem__(self, key):

return self.get(key)

  

def __contains__(self, key):

if self._get(key, self.root):

return True

else:

return False

  

def remove(self, currentNode):

if currentNode.isLeaf():

# 没有子节点的方法，直接删除

if currentNode == currentNode.parent.leftChild:

currentNode.parent.leftChild = None

else:

currentNode.parent.rightChild = None

elif currentNode.hasBothChildren():

succ = currentNode.findSuccessor()

succ.spliceOut()

currentNode.key = succ.key

currentNode.payload = succ.payload

else:

if currentNode.hasLeftChild():

if currentNode.isLeftChild():

# 左子节点删除

currentNode.leftChild.parent = currentNode.parent

currentNode.parent.leftChild = currentNode.leftChild

elif currentNode.isRightChild():

# 右子节点删除

currentNode.leftChild.parent = currentNode.parent

currentNode.parent.rightChild = currentNode.rightChild

else:

# 根节点删除

currentNode.replaceNodeData(

currentNode.leftChild,

currentNode.leftChild.payload,

currentNode.leftChild.leftChild,

currentNode.leftChild.rightChild,

)

else:

if currentNode.isLeftChild():

# 左子节点删除

currentNode.rightChild.parent = currentNode.parent

currentNode.parent.leftChild = currentNode.leftChild

elif currentNode.isRightChild():

# 右子节点

currentNode.rightChild.parent = currentNode.parent

currentNode.parent.rightChild = currentNode.rightChild

else:

# 根节点删除

currentNode.replaceNodeData(

currentNode.rightChild,

currentNode.rightChild.payload,

currentNode.rightChild.leftChild,

currentNode.rightChild.rightChild,

)

  

def delete(self, key):

if self.size > 1:

nodeToRemove = self._get(key, self.root)

if nodeToRemove:

self.remove(nodeToRemove)

self.size -= 1

else:

raise KeyError("nof found key")

  

elif self.size == 1 and self.root.key == key:

self.root = None

self.size -= 1

else:

raise KeyError("not found key")

  

def __delitem__(self, key):

self.delete(key)

  
  

if __name__ == "__main__":

myTree = BinarySearchTree()

# 字典传参数

myTree[3] = "red"

myTree[4] = "blue"

myTree[6] = "yellow"

myTree[2] = "at"

  

# 归属判断

print(3 in myTree)

# 索引

print(myTree[6])

  

# 删除

del myTree[3]

  

# 循环

for key in myTree:

print(key, myTree[key])
```

#### 树结构时间复杂度
![](readme.assets/Pasted%20image%2020230708232340.png)
### 图Graph
![](readme.assets/Pasted%20image%2020230708232634.png)
![](readme.assets/Pasted%20image%2020230708232705.png)
#### 六度分割理论
![](readme.assets/Pasted%20image%2020230708232951.png)
#### 术语表
![](readme.assets/Pasted%20image%2020230708233019.png)
![](readme.assets/Pasted%20image%2020230708233039.png)
![](readme.assets/Pasted%20image%2020230708233058.png)
![](readme.assets/Pasted%20image%2020230708233117.png)
![](readme.assets/Pasted%20image%2020230708233140.png)
![](readme.assets/Pasted%20image%2020230708233317.png)
#### 图抽象数据类型
ADT Graph实现的方法有两种主要形式：
-  邻接矩阵 adjacency matrix
![](readme.assets/Pasted%20image%2020230708234242.png)
![](readme.assets/Pasted%20image%2020230708234341.png)
简单实现
```python
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
```
实现方式
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

class Graph(object):

def __init__(self):

self.vertList = {}

self.numVertices = 0

  

def addVertex(self, key):

self.numVertices = self.numVertices + 1

newVertex = Vertex(key)

self.vertList[key] = newVertex

return newVertex

  

def getVertex(self, n):

if n in self.vertList:

return self.vertList[n]

else:

return None

  

def __contains__(self, n):

return n in self.vertList

  

def addEdge(self, f, t, cost=0):

# 为每个顶点设置权重

if f not in self.vertList:

nv = self.addVertex(f)

if t not in self.vertList:

nv = self.addVertex(t)

self.vertList[f].addNeighbor(self.vertList[t], cost)

  

def getVertices(self):

return self.vertList.keys()

  

def __iter__(self):

return iter(self.vertList.values())

  
  

class Vertex:

def __init__(self, key):

self.id = key

self.connectedTo = {}

  

def addNeighbor(self, nbr, weight=0):

self.connectedTo[nbr] = weight

  

def __str__(self) -> str:

return str(self.id) + "connectedTo: " + str([x.id for x in self.connectedTo])

  

def getConnectedTo(self):

return self.connectedTo.keys()

  

def getId(self):

return self.id

  

def getWeight(self, nbr):

return self.connectedTo[nbr]

  
  

if __name__ == "__main__":

g = Graph()

for i in range(6):

g.addVertex(i)

  

# 获取列表结构

print(g.vertList)

  

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

for w in v.getConnectedTo():

print("(%s, %s)" % (v.getId(), w.getId()))

```

-  邻接表 adjacent list
![](readme.assets/Pasted%20image%2020230708234406.png)
#### 词梯问题
![](readme.assets/Pasted%20image%2020230709003704.png)
![](readme.assets/Pasted%20image%2020230709004019.png)
#### 广度优先搜索BFS
![](readme.assets/Pasted%20image%2020230709004919.png)
![](readme.assets/Pasted%20image%2020230709004933.png)
![](readme.assets/Pasted%20image%2020230709005155.png)
分桶存放
![](readme.assets/Pasted%20image%2020230709005227.png)
避免走重复路，所以需要标记。
![](readme.assets/Pasted%20image%2020230709131001.png)
```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

"""

! 如何将大量的单词放入到图中：

1.将单词作为顶点的key，如果两个单词之间只相差一个字母，就在他们之间设置一条边

2.无向图==顶点之间没有权重

"""

from pythonds.graphs.adjGraph import Graph

from pythonds.basic.queue import Queue

import os

  
  

def buildGraph(wordFile):

d = {}

g = Graph()

# 获取四字母单词集

wfile = open(wordFile, "r")

for line in wfile:

word = line.strip()

for i in range(len(word)):

bucket = word[:i] + "-" + word[i + 1 :]

if bucket in d:

d[bucket].append(word)

else:

d[bucket] = [word]

  

for bucket in d.keys():

for word1 in d[bucket]:

for word2 in d[bucket]:

if word1 != word2:

g.addEdge(word1, word2)

  

return g

  
  

# BFS算法

def bfs(g, start):

start.setDistance(0)

start.setPred(None)

# 设置队列

vertQueue = Queue()

vertQueue.enqueue(start)

while vertQueue.size() > 0:

# 取队首作为当前顶点

currentVert = vertQueue.dequeue()

for nbr in currentVert.getConnections():

# 遍历临街顶点

if nbr.getColor() == "white":

nbr.setColor("gray")

nbr.setDistance(currentVert.getDistance() + 1)

nbr.setPred(currentVert)

vertQueue.enqueue(nbr)

# 设置当前顶点为黑色

currentVert.setColor("black")

  
  

def traverse(y):

x = y

while x.getPred():

print(x.getId())

x = x.getPred()

print(x.getId())

  
  

if __name__ == "__main__":

xpth = os.path.dirname(os.path.abspath(__file__))

os.chdir(xpth)

wordgraph = buildGraph("./word.txt")

bfs(wordgraph, wordgraph.getVertex("FOOL"))

traverse(wordgraph.getVertex("SAGE"))
```

#### 骑士周游问题
![](readme.assets/Pasted%20image%2020230709133502.png)
#### 深度优先搜索DFS
![](readme.assets/Pasted%20image%2020230709141007.png)


```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  

from pythonds.graphs.adjGraph import Graph

from pythonds.basic.stack import Stack

  
  

def genLegalMoves(x, y, bdSize):

newMoves = []

# 马的八种走法

moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

  

for i in moveOffsets:

newX = x + i[0]

newY = y + i[1]

if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):

newMoves.append((newX, newY))

  

return newMoves

  
  

def legalCoord(x, bdSize):

# 确认不走出棋盘

if x >= 0 and x <= bdSize:

return True

else:

return False

  
  

def knightGraph(bdSize):

ktGraph = Graph()

for row in range(bdSize):

# 遍历每个格子

for col in range(bdSize):

nodeId = posToNodeId(row, col, bdSize)

# 单步合法走棋

newPositions = genLegalMoves(row, col, bdSize)

for e in newPositions:

nid = posToNodeId(e[0], e[1], bdSize)

# 添加边及顶点

ktGraph.addEdge(nodeId, nid)

return ktGraph

  
  

def posToNodeId(row, col, bdSize):

return row * bdSize + col

  
  

def knightTour(n, path, u, limit):

# n层次，path路径，u顶点，limit深度

u.setColor("gray")

# 当前顶点加入路径

path.append(u)

  

if n < limit:

# 对所有合法移动逐一深入

nbrList = list(u.getConnections())

i = 0

done = False

while i < len(nbrList) and not done:

# 选择白色未经过顶点深入

if nbrList[i].getColor() == "white":

# 层次加一，递归深入

done = knightTour(n + 1, path, nbrList[i], limit)

i += 1

if not done:

# 都无法完成总深度，回溯，试本层下一个顶点

path.pop()

u.setColor("white")

else:

done = True

return done
```
算法改进 Warnsdorff
![](readme.assets/Pasted%20image%2020230709143743.png)

```python
def orderByAvail(n):
	
	resList = []
	
	for v in n.getConnections():
	
	if v.getColor() == "white":
	
	c = 0
	
	for w in v.getConnections():
	
	if w.getColor() == "white":
	
	c += 1
	
	resList.append((c, v))
	
	resList.sort(key=lambda x: x[0])
	
	return [y[1] for y in resList]

```

##### 通用深度优先搜索算法
![](readme.assets/Pasted%20image%2020230709144001.png)
深度优先森林
![](readme.assets/Pasted%20image%2020230709144024.png)

```python
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
```


#### topological sort 拓扑排序
![](readme.assets/Pasted%20image%2020230709151643.png)
![](readme.assets/Pasted%20image%2020230709151908.png)
![](readme.assets/Pasted%20image%2020230709152141.png)
结束时间倒序
![](readme.assets/Pasted%20image%2020230709152201.png)
#### 强连通分支
![](readme.assets/Pasted%20image%2020230709152629.png)
聚类算法：离散数据集合，通过一定的条件，拆分称为多个子集，每个子集存在一个质心，这个质心就可以代表真个子集。然后让整个集合的数据量减少。
![](readme.assets/Pasted%20image%2020230709152948.png)

![](readme.assets/Pasted%20image%2020230709153029.png)
![](readme.assets/Pasted%20image%2020230709153228.png)
#### 最短路径
![](readme.assets/Pasted%20image%2020230709153616.png)
![](readme.assets/Pasted%20image%2020230709153634.png)
```shell
$ traceroute ip
traceroute www.baidu.com

traceroute: Warning: www.baidu.com has multiple addresses; using 104.193.88.77
traceroute to www.wshifen.com (104.193.88.77), 64 hops max, 52 byte packets

 1  * * *

 2  172.20.21.254 (172.20.21.254)  213.519 ms  215.708 ms  234.393 ms

 3  172.20.22.3 (172.20.22.3)  222.874 ms  218.175 ms  223.813 ms

 4  * * *

 5  38.132.97.153 (38.132.97.153)  239.556 ms  235.334 ms  226.373 ms

 6  * * 146.70.0.211 (146.70.0.211)  214.701 ms

 7  ewr-b2-link.ip.twelve99.net (62.115.183.76)  226.584 ms

    ewr-b2-link.ip.twelve99.net (62.115.62.253)  247.564 ms

    ewr-b2-link.ip.twelve99.net (62.115.185.176)  232.204 ms

 8  nyk-bb2-link.ip.twelve99.net (62.115.136.46)  225.800 ms

    nyk-bb2-link.ip.twelve99.net (62.115.140.192)  219.121 ms

    nyk-bb1-link.ip.twelve99.net (62.115.136.44)  220.213 ms

 9  rest-bb1-link.ip.twelve99.net (62.115.141.244)  230.489 ms  235.732 ms  244.838 ms
```
可以列出经过的所有路由和服务。
![](readme.assets/Pasted%20image%2020230709155416.png)
![](readme.assets/Pasted%20image%2020230709155548.png)
![](readme.assets/Pasted%20image%2020230709160142.png)
![](readme.assets/Pasted%20image%2020230709160211.png)
https://zhuanlan.zhihu.com/p/45062599
- 现代计算机网络通常使用动态路由算法，因为这类算法能够适应网络的拓扑和流量变化，其中最流行的两种动态路由算法是“距离矢量路由算法”和“链路状态路由算法”。
	- 距离矢量路由算法（Distance Vector Routing，DV）是ARPANET网络上最早使用的路由算法，也称Bellman-Ford路由算法和Ford-Fulkerson算法，主要在RIP（Route Information Protocol）协议中使用。Cisco的IGRP和EIGRP路由协议也是采用DV这种路由算法的。
		- “距离矢量路由算法”的基本思想如下：每个路由器维护一个距离矢量（通常是以延时是作变量的）表，然后通过相邻路由器之间的距离矢量通告进行距离矢量表的更新。每个距离矢量表项包括两部分：到达目的结点的最佳输出线路，和到达目的结点所需时间或距离，通信子网中的其它每个路由器在表中占据一个表项，并作为该表项的索引。每隔一段时间，路由器会向所有邻居结点发送它到每个目的结点的距离表，同时它也接收每个邻居结点发来的距离表。这样以此类推，经过一段时间后便可将网络中各路由器所获得的距离矢量信息在各路由器上统一起来，这样各路由器只需要查看这个距离矢量表就可以为不同来源分组找到一条最佳的路由。
		- 优点：非常简单清晰，且任何加入到网络中的新节点都能很快的与其它节点建立起联系获得补充信息。
		- 缺点:    首先就是每次发送信息的时候，要发送整个全局路由表，太大了，因为每个路由器需要在矢量表中记录下整个网络的信息，导致需要较大存储、CPU、网络开销，对资源的要求越来越高。还有一个问题就是收敛时间太慢，也就是路由器共享路由信息并使各台路由器掌握的网络情况达到一致所需的时间比较久，收敛速度慢会导致有些路由器的表更新慢，从而造成路由环路的问题。
	-  链路状态路由算法（Link State Routing ），基于Dijkstra算法，它是以图论作为理论基础，用图来表示网络拓扑结构，用图论中的最短路径算法来计算网络间的最佳路由。基于这类算法实现的协议有：OSPF 等。
		- 这类算法的基本思路是：采用的是不停的拼接地图的方式。每一个路由器首先都会发现自己身边的邻居节点，然后将自己与邻居节点之间的链路状态包广播出去，发送到整个网络。这样，当某个路由器收到从网络中其它路由器广播来的路由信息包（链路状态包）之后，会将这个包中的信息与自己路由器上的信息进行拼装，最终形成一个全网的拓扑视图。
		- 当路由器中形成了全网的拓扑视图后，它就可以通过最短路径算法来计算当前节点到其它路由器之间的最短路径了。当某台路由器的链路状态发生变化时，路由器采用洪泛法向所有路由器发送此信息，其它路由器使用收到的信息重新计算最佳路径，重新生成路由表（拓扑图）。
		- 这里可以做一个类比，有一个路人甲人去问路，然后本地人A只知道A自己生活方圆5公里的地图，本地人B只知道B自己生活的方圆5公里的地图，但是路人甲要去的地方需要穿过A和B所在区域，那么就把A和B的2份地图拿来拼装在一起，然后去往目的地的完整路线就可以查出来了。

```python
#!/usr/bin/python

# -*- coding: utf-8 -*-

  
  

def Dijkstra(G, start):

# 输入是从 0 开始，所以起始点减 1

start = start - 1

inf = float("inf")

node_num = len(G)

# visited 代表哪些顶点加入过

visited = [0] * node_num

# 初始顶点到其余顶点的距离

dis = {node: G[start][node] for node in range(node_num)}

# parents 代表最终求出最短路径后，每个顶点的上一个顶点是谁，初始化为 -1，代表无上一个顶点

parents = {node: -1 for node in range(node_num)}

# 起始点加入进 visited 数组

visited[start] = 1

# 最开始的上一个顶点为初始顶点

last_point = start

  

for i in range(node_num - 1):

# 求出 dis 中未加入 visited 数组的最短距离和顶点

min_dis = inf

for j in range(node_num):

if visited[j] == 0 and dis[j] < min_dis:

min_dis = dis[j]

# 把该顶点做为下次遍历的上一个顶点

last_point = j

# 最短顶点假加入 visited 数组

visited[last_point] = 1

# 对首次循环做特殊处理，不然在首次循环时会没法求出该点的上一个顶点

if i == 0:

parents[last_point] = start + 1

for k in range(node_num):

if G[last_point][k] < inf and dis[k] > dis[last_point] + G[last_point][k]:

# 如果有更短的路径，更新 dis 和 记录 parents

dis[k] = dis[last_point] + G[last_point][k]

parents[k] = last_point + 1

  

# 因为从 0 开始，最后把顶点都加 1

return {key + 1: values for key, values in dis.items()}, {key + 1: values for key, values in parents.items()}

  
  

if __name__ == "__main__":

inf = float("inf")

G = [[0, 1, 12, inf, inf, inf], [inf, 0, 9, 3, inf, inf], [inf, inf, 0, inf, 5, inf], [inf, inf, 4, 0, 13, 15], [inf, inf, inf, inf, 0, 4], [inf, inf, inf, inf, inf, 0]]

dis, parents = Dijkstra(G, 1)

print("dis: ", dis)

print("parents: ", parents)
```




#### 最小生成树 smallest tree
![](readme.assets/Pasted%20image%2020230709161131.png)
单播解法：流量负担。
![](readme.assets/Pasted%20image%2020230709161228.png)
洪水解法：会造成洪范攻击。
![](readme.assets/Pasted%20image%2020230709161257.png)
![](readme.assets/Pasted%20image%2020230709161346.png)
生成树：图解最优解。
![](readme.assets/Pasted%20image%2020230709161411.png)
![](readme.assets/Pasted%20image%2020230709161455.png)
![](readme.assets/Pasted%20image%2020230709161525.png)
```python
from pythonds.graphs import PriorityQueue, Graph, Vertex

import sys

  
  

def prim(G, start):

pq = PriorityQueue()

for v in G:

v.setDistance(sys.maxsize)

v.setPred(None)

start.setDistance(0)

pq.buildHeap([(v.getDistance(), v) for v in G])

while not pq.isEmpty():

currentVert = pq.delMin()

for nextVert in currentVert.getConnections():

newCost = currentVert.getWeight(nextVert)

if nextVert in pq and newCost < nextVert.getDistance():

nextVert.setPred(currentVert)

nextVert.setDistance(newCost)

pq.decreaseKey(nextVert, newCost)
```

## 什么是算法分析？

算法的实现，根据需求实现目的。（这个是算法的根本）
算法的好坏，在于计算消耗的资源。（这个是算法的优化）

### 时间复杂度：

「 **大O符号表示法** 」，即 T(n) = O(f(n))
f(n)的函数，求导之后的就知道，对T的斜率影响最大的那个部分是哪一部分了，必然是指数最大那个阶级。
![](Pasted%20image%2020230405201717.png)
![](Pasted%20image%2020230405201831.png)
**常见的时间复杂度量级有：**
-   常数阶O(1)
-   对数阶O(logN)
-   线性阶O(n)
-   线性对数阶O(n * logN)
-   平方阶O(n²)
-   立方阶O(n³)
-   K次方阶O(n^k)
-   指数阶O(2^n) 上面从上至下依次的时间复杂度越来越大，执行的效率越来越低。
-   阶乘阶O(n!)
#### 常数阶O(1)
```python
def constant(n: int) -> int:
    """常数阶"""
    count: int = 0
    size: int = 100000
    for _ in range(size):
        count += 1
    return count

```
#### 对数阶O(logN)
```python
def logarithmic(n: float) -> int:
    """对数阶（循环实现）"""
    count: int = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

```

#### 线性阶O(n)
```python
def linear(n: int) -> int:
    """线性阶"""
    count: int = 0
    for _ in range(n):
        count += 1
    return count

```

#### 线性对数阶O(n * logN)
```python
def linear_log_recur(n: float) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    count: int = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count
```

#### 平方阶O(n²)
```python
def quadratic(n: int) -> int:
    """平方阶"""
    count: int = 0
    # 循环次数与数组长度成平方关系
    for i in range(n):
        for j in range(n):
            count += 1
    return count

```
#### 立方阶O(n³)
```python
def quadratic(n: int) -> int:
    """平方阶"""
    count: int = 0
    # 循环次数与数组长度成平方关系
    for i in range(n):
        for j in range(n):
            for z in range(n):
	            count += 1
    return count

```

#### K次方阶O(n^k)
```python

k = 10Ï

def demo(n: int = 10, c: int = 0, result: int = []) -> int:

"""K次方阶(递归实现）"""

if c == k:

return

for i in range(n):

c += 1

n -= 1

result.append(i)

demo(n, c, result)

```

#### 指数阶O(2^n)
```python
def exponential(n: int) -> int:
    """指数阶（循环实现）"""
    count: int = 0
    base: int = 1
    # cell 每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + .. + 2^(n-1) = 2^n - 1
    return count

```

#### 阶乘阶O(n!)
```python
def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count: int = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count
```


### 空间复杂度：

-  常数阶O(1)
-  对数阶O(log n)
-  线性阶O(n)
-  平方阶O(n^2)
-  指数阶O(2^n)

#### 常数阶O(1)
```python
def constant(n: int) -> None:
    """常数阶"""
    # 常量、变量、对象占用 O(1) 空间
    a: int = 0
    nums: list[int] = [0] * 10000
    node = ListNode(0)
    # 循环中的变量占用 O(1) 空间
    for _ in range(n):
        c: int = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()

```

#### 对数阶O(log n)
```python
def logarithmic(n: float) -> int:
    """对数阶（循环实现）"""
    count: int = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

```

#### 线性阶O(n)
```python
def linear(n: int) -> None:
    """线性阶"""
    # 长度为 n 的列表占用 O(n) 空间
    nums: list[int] = [0] * n
    # 长度为 n 的哈希表占用 O(n) 空间
    mapp = dict[int, str]()
    for i in range(n):
        mapp[i] = str(i)

```

#### 平方阶O(n^2)

```python
def quadratic(n: int) -> None:
    """平方阶"""
    # 二维列表占用 O(n^2) 空间
    num_matrix: list[list[int]] = [[0] * n for _ in range(n)]

```

#### 指数阶O(2^n)
```python
def build_tree(n: int) -> TreeNode | None:
    """指数阶（建立满二叉树）"""
    if n == 0:
        return None
    root = TreeNode(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n - 1)
    return root

```