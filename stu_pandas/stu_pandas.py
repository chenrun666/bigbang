"""
筛选出转航班的航段，进行出发时间和到达时间的拼接，变成一个航段
实现思路： 利用pandas的series模块，对数据进行重复筛选，返回bool，再通过itertools的compress，进行比较，取出是True的航段
"""

import pandas as pd

import operator

from itertools import compress

# a = [("john", "A", 15), ("jane", "B", 12), ("dave", "B", 10)]
# c = sorted(a, key=operator.itemgetter(1, 2))
# print(c)

item = [{"flightNum": "FD123123", "dep": "123"}, {"flightNum": "FD0987", "dep": "000"},
        {"flightNum": "FD123123", "dep": "456"}, {"flightNum": ""}]
# 取出对应的值
c = map(operator.itemgetter("flightNum"), item)
# print([item for item in c])

# 达到相同的效果
d = [tmp["flightNum"] for tmp in item]
# print(d)

e = pd.Series(map(operator.itemgetter("flightNum"), item)).duplicated(keep=False).tolist()
double = list(compress(item, e))
# print(double)

f = pd.Series(map(operator.itemgetter("flightNum"), item)).tolist()  # 去除空值
print(list(compress(item, f)))



