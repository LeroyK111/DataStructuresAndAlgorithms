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
