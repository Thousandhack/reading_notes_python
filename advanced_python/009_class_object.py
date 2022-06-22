#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
类变量与实例化变量
"""


class A:
    """
    类变量
    """
    aa = 1

    def __init__(self, x, y):
        """
        实例化对象变量
        :param x:
        :param y:
        """
        self.x = x
        self.y = y


a = A(2, 4)
print(a.x, a.y, a.aa)
"""
修改了类变量对于的实例化的类变量也会跟着改变
"""
A.aa = 11
print(a.x, a.y, a.aa)

"""
赋值实例化对象变量的话，不应该类变量
在这个例子中就是：
    a.xx 赋值不改变  A.aa
    A.aa 赋值会改变  a.aa
"""
a.x = 5
a.y = 6
a.aa = 100

print(a.x, a.y, a.aa, A.aa)
