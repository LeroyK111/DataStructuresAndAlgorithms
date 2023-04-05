#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def anagramSolution1(self, s1, s2):
        """
        逐字检查
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


if __name__ == "__main__":
    S = Solution()
    result1 = S.anagramSolution1("abcd", "dcab")
    print(result1)
 