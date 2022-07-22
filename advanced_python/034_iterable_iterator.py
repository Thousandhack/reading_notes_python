#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
什么是迭代器和可迭代对象

"""
from collections.abc import Iterator


class Company(object):
    """
    这是一个可迭代对象
    """
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        """
        调用自定义迭代器
        :return:
        """
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    """
    实现自定义迭代器
    """
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])
    iter_demo = iter(company)
    # while True:
    #     try:
    #         print(next(iter_demo))
    #     except:
    #         pass
    for demo in iter_demo:
        print(demo)