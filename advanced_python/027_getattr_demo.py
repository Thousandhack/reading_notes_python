#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


"""
1.__getattr__
    getattr用法 ： getattr(对象,属性,如果没有属性的话赋对应的值)
    age = getattr(user, "age", 15)
    print(age)
2.__getattribute__  不管调用什么属性，直接先到 __getattribute__
"""

from datetime import date, datetime


class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        """
        找不到会进这个方法
        :param item:
        :return:
        """
        return self.info[item]

    # def __getattribute__(self, item):
    #     """
    #     少用
    #     :param item:
    #     :return:
    #     """
    #     return None


if __name__ == "__main__":
    user = User("hsz", date(year=1994, month=5, day=3), info={"company_name": "MYY", "company_address": "sz"})
    print(user.birthday)
    print(user.company_name)
    print(user.company_address)


