#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
python 的自省机制
"""

class Person:
    name = "user"


class Student(Person):

    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("一中")

    #  通过__dict__ 查询属性
    print(user.__dict__)
    print(Person.__dict__)
    # 列出对象的所有属性
    print(dir(user))
