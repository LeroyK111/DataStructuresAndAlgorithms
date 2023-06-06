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