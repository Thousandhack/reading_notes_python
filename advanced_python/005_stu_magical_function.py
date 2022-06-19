#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
ipython 使用

pip install notebook



非数学运算
    字符串表示
    __repr__
    __str__
    集合、序列相关
    __len__,getitem__,__setitem__,__delitem__,__contains__
    迭代相关
    __iter__,__next__
    可调用
    __call__
    with上下文管理器
    __enter__
    __exit__
    数值转换
    __abs__,__bool__,__init__,__float__,__hash__,__index__,__new__
    元类相关
    __new__
    __init__
    属性相关
    __get__
    __set__
    __delete__

    协程
    __await__
    __aiter__
    __aenter__
    __aexit__

数学运算
    一元运算符
    __neg__
    __pos__
    __abs__
    二元运算符
    __lt__
    __le__
    __eq__
    __ne__
    __gt__
    __ge__
    算术运算符
    __add__
    __sub__
    __mul__
    __truediv__
    __floordiv__
    __mod__
    __divmod__
    __pow__
    __round__

    反向算术运算符
    __radd__
    _rsub__


"""


class Company(object):

    def __init__(self, employee_list):
        """
        初始化名称列表
        :param employee_list:
        """
        self.employee = employee_list

    def __repr__(self):
        """
        开发模式 使用
        :return:
        """
        return ",".join(self.employee)

    # def __str__(self):
    #     """
    #     对 对象进行字符串格式化
    #     :return:
    #     """
    #     return ",".join(self.employee)


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        """
        x，y 值的相加
        :param other_instance:
        :return:
        """
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x},y:{y}".format(x=self.x, y=self.y)


if __name__ == "__main__":
    company = Company(["tom", "hsz", "ming"])

    # print(company)
    #
    print(company.__repr__())

    first_vec = MyVector(1, 2)
    second_vec = MyVector(2, 3)
    print(first_vec + second_vec)
