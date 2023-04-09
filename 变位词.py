#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def anagramSolution1(self, s1, s2):
        """
        逐字检查, 双循环n^2
        """
        alist = list(s2)
        pos1 = 0
        stillOK = True
        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    # 让s2逐个比较
                    found = True
                else:
                    pos2 += 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False
            pos1 += 1

        return stillOK

    def anagramSolution2(self, s1, s2):
        """
        排序比较，单循环 n
        """
        alist1 = list(s1)
        alist2 = list(s2)
        # 隐藏一个排序算法，n log n
        alist1.sort()
        alist2.sort()
        pos = 0
        matches = True
        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos += 1
            else:
                matches = False

        return matches

    """
    暴力法：n!的阶乘，穷举所有的组合，然后查看有没有s2的存在。不推荐
    """

    def anagramSolution4(self, s1, s2):
        """
        计数比较
        """
        c1 = [0] * 26
        c2 = [0] * 26
        for i in range(len(s1)):
            # ord查询unicode 字符串对应的位置
            pos = ord(s1[i] - ord("a"))
            c1[pos] = c1[pos] + 1
        for i in range(len(s2)):
            pos = ord(s2[i] - ord("a"))
            c2[pos] = c2[pos] + 1

        j = 0
        stillOK = True
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                stillOK = False

        return stillOK


if __name__ == "__main__":
    S = Solution()
    result1 = S.anagramSolution1("abcd", "dcab")
    result2 = S.anagramSolution2("abcd", "dcb")
    print(result1, result2)
