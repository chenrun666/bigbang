"""
python3.x 中已经没有cmp函数。需要导入operator
"""
import operator

a = operator.eq("123", "123")
a = operator.lt("123", "12")  # low than
a = operator.le("12", "12")  # low or eq
a = operator.ne("12", "12")  # not eq
a = operator.ge("12", "10")  # great or eq
a = operator.gt("12", "12")  # great than
print(a)