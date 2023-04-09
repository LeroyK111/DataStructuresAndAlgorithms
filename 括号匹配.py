from pythonds.basic.stack import Stack

"""
使用pythonds库直接构造栈的对象。
"""


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == close.index(close)


def parChecker(symobolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symobolString) and balanced:
        symbol = symobolString[index]
        if symbol == "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                # 删除对应的')'
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker("(()))"))
