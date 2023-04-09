#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    openrandStack = Stack()
    tokenList = list(postfixExpr)
    for token in tokenList:
        if token in string.digits:
            openrandStack.push(int(token))
        else:
            # 符号
            operand2 = openrandStack.pop()
            operand1 = openrandStack.pop()
            # 计算
            result = doMath(token, operand1, operand2)
            openrandStack.push(result)
    return openrandStack.pop()


def doMath(op, op1, op2):
    match op:
        case "+":
            return op1 + op2
        case "-":
            return op1 - op2
        case "*":
            return op1 * op2
        case "/":
            return op1 / op2

"""
输入后缀字符，则执行计算
"""
print(postfixEval("23*1+"))
