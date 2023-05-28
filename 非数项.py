#!/usr/bin/python
# -*- coding: utf-8 -*-


def hashStr(data, slot):
    result = []
    for i, v in enumerate(data):
        # 加入权重
        result.append(ord(v) * i)

    done = sum(result)
    # 开始散列
    index = done % len(slot)
    slot[index] = data

    return slot


if __name__ == "__main__":
    data = "asdsdaf"
    slot = [None for i in range(11)]
    print(hashStr(data, slot))
