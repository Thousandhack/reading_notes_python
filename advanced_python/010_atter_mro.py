#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
查找顺序由下而上
mro 算法

深度优先
广度优先
C3 算法
"""

# 版本1：
# class D:
#     pass
#
#
# class C(D):
#     pass
#
#
# class B(D):
#     pass
#
#
# class A(B, C):
#     pass
#
#
# # 这个表示 类的继承顺序
# print(A.__mro__)
"""
        D
    B        C
        A
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
"""


# 版本2：
class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


# 这个表示 类的继承顺序
print(A.__mro__)
"""
    D       E
    B       C
        A
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
"""



