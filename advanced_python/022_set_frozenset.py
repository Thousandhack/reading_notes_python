#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
set 集合
forzenset  不可变集合

"""

s = set("assqabv")

print(s)

f_s = frozenset("abcddd")
print(f_s)

# set 更新数据
s.update(f_s)

print(s)


# difference 差集
ret_set = s.difference({"d", "c"})

print(ret_set)
# 判断一个集合是另外一个集合的子集
print(ret_set.issubset(s))
