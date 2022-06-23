#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import time

"""
私有属性，私有方法
"""

class User:

    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        now_time = time.strftime('%Y-%m-%d', time.localtime())
        year, month, day = tuple(now_time.split("-"))
        return int(year) - int(self.__birthday)


if __name__ == "__main__":
    user = User("1994")
    # user.__birthday    # __birthday 是调用不了的，它是私有属性，只能这个类调用
    print(user.get_age())
    # 从语言层面没有办法绝对的做到私有属性
    # 强制将私有属性调用出来
    # _classname__birthday
    # print(user._User__birthday)
