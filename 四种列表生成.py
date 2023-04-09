from timeit import timeit, Timer


def test1():
    ls = []
    for i in range(1000):
        ls += [i]


def test2():
    ls = []
    for i in range(1000):
        ls.append(i)


def test3():
    ls = [i for i in range(1000)]


def test4():
    ls = list(range(1000))



if __name__ == "__main__":
    t1 = timeit(test1, number=1000)
    print("concat %f seconds" % t1)
    t2 = timeit(test2, number=1000)
    print("append %f seconds" % t2)
    t3 = timeit(test3, number=1000)
    print("list concat %f seconds" % t3)  # 最快方法
    t4 = timeit(test4, number=1000)
    print("range %f seconds" % t4)    