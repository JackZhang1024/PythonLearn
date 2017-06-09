# -*- coding:utf-8 -*-
# 列表生成式
L = [x * x for x in range(10)]
for i in L:
    print(i)
M = (x * x for x in range(10))
for n in M:
    print(n)


# generator

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'


# for n in fib(10):
#     print(n)

# g = fib(10)
# while True:
#     try:
#         x = next(g)
#         print('g', x)
#     except StopIteration as e:
#         print('Generator return value ', e.value)


# 杨辉三角问题

#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1
def triangles():
    L=[1]
    while True:
         yield L
         L.append(0)
         L = [L[i - 1] + L[i] for i in range(len(L))]
for line in triangles():
    if len(line)>6:break
    print(line)