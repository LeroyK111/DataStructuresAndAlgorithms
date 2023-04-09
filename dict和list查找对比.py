from timeit import Timer
import random


for i in range(10000, 1000001, 20000):
    t = Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    # !字典执行时间是常数，列表执行则线性增长。
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))
