#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
isinstance 和 type
在开发中，能使用isinstance 不要去使用type

"""


class A:
    pass


class B:
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))



