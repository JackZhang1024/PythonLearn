# -*- coding:utf-8 -*-

"""
阶乘算法
"""


def recursion(n):
    if n == 1:
        return 1
    else:
        return n*recursion(n-1)

result = recursion(5)
print(result)
