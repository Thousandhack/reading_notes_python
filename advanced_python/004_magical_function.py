#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
魔法函数
python的类里面以双下划线为开头的和双下划线结尾的函数称为魔法函数。

魔法函数要使用python提供的魔法函数。

例子说明魔法函数的重要性比如len函数

"""


class Company(object):

    def __init__(self, employee_list):
        """
        初始化名称列表
        :param employee_list:
        """
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)



company = Company(["tom", "hsz", "ming"])

# employee = company.employee
#
# for em in employee:
#     print(em)

for em in company:
    print(em)


print(len(company))