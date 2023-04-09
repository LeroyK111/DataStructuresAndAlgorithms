#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythonds.basic.stack import Stack
import string

"""
操作符对计算顺序的影响:
前缀表达式：+AB
后缀表达式：AB-
中缀表单式：C+(A*B)

! 我们都应该避免中缀表达式，将中缀表达式转后缀表单式
"""


def infixToPostfix(x: str) -> str:
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = list(x)

    for token in tokenList:
        print(token)
        print(postfixList)
        print(opStack.items, "\n")
        # 从左向右读
        if token in string.ascii_uppercase or token in string.digits:
            # 读到数字和字母就进列表
            postfixList.append(token)
        elif token == "(":
            # 读到中缀就进栈
            opStack.push(token)
        elif token == ")":
            # 读到右括号就弹出一个左括号
            topToken = opStack.pop()
            while topToken != "(":
                # 如果不是左括号，就加入列表
                postfixList.append(topToken)
                # 然后继续弹出
                topToken = opStack.pop()
        else:
            # 读到符号，栈不为空，且栈顶符号优先级大于等于此刻的符号
            while (not opStack.isEmpty()) and prec[opStack.peek()] >= prec[token]:
                # 栈弹出，并且加入list
                postfixList.append(opStack.pop())
            # 将等级低的加入堆栈中
            opStack.push(token)

    while not opStack.isEmpty():
        # 在判断是否为空，不为空，我们就把剩余栈数据写入list
        postfixList.append(opStack.pop())
    # 返回 字符串
    return " ".join(postfixList)



print(infixToPostfix("A*B+1"))
