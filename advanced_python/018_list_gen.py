#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
列表生成式（列表推导式）
# 1. 提取出1-20之间的奇数
"""

odd_list = []
for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)

odd_list = [i for i in range(21) if i % 2 == 1]

# 列表生成式性能高于列表操作
print(type(odd_list))
print(odd_list)


# 2. 逻辑复杂的情况

def handle_item(item):
    return item * item


# 生成器表达式
odd_gen = (handle_item(i) for i in range(21) if i % 2 == 1)
print(type(odd_gen))
print(odd_gen)
for item in odd_gen:
    print(item)

odd_to_list = list(odd_gen)

# 字典推导式
my_dict = {"hsz": 28, "wcc": "27"}
# 将键值颠倒
reversed_dict = {value: key for key, value in my_dict.items()}

print(reversed_dict)

# 集合推导式
the_set = {key for key, _ in my_dict.items()}
print(type(the_set))
print(the_set)
