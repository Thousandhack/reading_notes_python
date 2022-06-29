#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
1.cpython 中垃圾回收的算法是采用 引用计数

"""

a = 1
b = a
del a  # 引用计数 减 1
print(b)


class A:
    def __del__(self):
        pass
