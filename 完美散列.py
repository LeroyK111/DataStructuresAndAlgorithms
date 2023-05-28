#!/usr/bin/python
# -*- coding: utf-8 -*-


import hashlib as hs


def md5(str):
    return hs.md5(str).hexdigest()


def sha1(str):
    return hs.sha1(str).hexdigest()


def md5Step(str):
    m = hs.md5()
    m.update(str)

    return m.hexdigest()


if __name__ == "__main__":
    message = "Hello, world!".encode("utf-8")
    print(message)
    print(md5(message))
    print(sha1(message))
    print(md5Step(message))
