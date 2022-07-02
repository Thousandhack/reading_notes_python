#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
1.property 动态属性

"""

from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):
        """
        property 将函数的 变成属性描述符的方法
        :return:
        """
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value



if __name__ == "__main__":
    user = User("hsz", date(year=1994, month=5, day=3))
    print(user.name)
    print(user.birthday)
    print(user.age)
    user.age = 25
    print(user.age)
