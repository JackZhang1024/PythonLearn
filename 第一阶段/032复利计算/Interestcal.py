# -*- coding:utf-8 -*-

"""
m是第一年投入的本金
l是每年投入的等额金额
n是计算的年数
r是利率的百分比
"""


def calculate(m, n, r, l=10000):
    if n == 0:
        result = m
        print("年份 %02d 最终资产 %.3f  收益增长 %.3f" % (n, result, 0))
        return m
    if n == 1:
        result = m*(1+r)
        print("年份 %02d  最终资产 %.3f 收益增长 %.3f 累计收益 %.3f 累计投入资本 %.3f"
              % (n, result, result-calculate(m, n-1, r, l), result-m-0, m))
        return result
    if n > 1:
        result = float(calculate(m, n - 1, r, l))
        final = (result + l)*(1+r)
        print("年份 %02d  最终资产 %.3f 收益增长 %.3f 累计收益 %.3f 累计投入资本 %.3f"
              % (n, final, final-result-l, final-m-(n-1)*l, (m + (n-1)*l)))
        return final

total = calculate(100000, 20, 0.0365, 30000)
print(total)
