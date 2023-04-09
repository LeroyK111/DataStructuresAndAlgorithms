#!/usr/bin/python
# -*- coding: utf-8 -*-
from timeit import Timer

# pop0 则是线性增长的
popzero = Timer("x.pop(0)", "from __main__ import x")

# pop 是平坦的常数
popend = Timer("x.pop()", "from __main__ import x")

for i in range(10**7, 10**7 + 1, 10**6):
    x = list(range(i))
    # 执行函数
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz, pt))



