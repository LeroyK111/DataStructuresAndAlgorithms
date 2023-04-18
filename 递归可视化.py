#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

"""
forward
backward
left
right
penup
pendown
pensize
pencolor
"""

t = turtle.Turtle()
# !画一条线
# t.forward(100)

# !画一个矩形
for i in range(4):
    t.forward(100)
    t.right(90)

# !五角星
t.pencolor("red")
t.pensize("3")
for i in range(5):
    t.forward(100)
    t.right(144)
# 隐藏箭头图标
t.hideturtle()


# 递归螺旋
def drawSpiral(t, linelen):
    if linelen > 0:
        # 最小规模
        t.forward(linelen)
        t.right(90)
        # 递减
        drawSpiral(t, linelen - 5)


drawSpiral(t, 100)






# 结束绘图
turtle.done()
