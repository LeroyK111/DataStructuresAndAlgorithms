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
算法+数据机构=程序
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
-   指数阶(2^n) 上面从上至下依次的时间复杂度越来越大，执行的效率越来越低。
















### 空间复杂度：

-  常数阶O(1)
-  对数阶O(log n)
-  线性阶O(n)
-  平方阶O(n^2)
-  指数阶O(2^n)








