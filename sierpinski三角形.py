#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()


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
