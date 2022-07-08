#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
__new__ 和 __init__ 区别

最根本的区别是__new__是可以自定义 类的生成的过程的 （cls 传递进来的是类）
__init__ 方法传递进来的是 （实例化对象）对象

new传递进来的是类，而且这个时候对象是还没有生成的

"""


class User:

    def __new__(cls, *args, **kwargs):
        """
        可以在生成对象之前加逻辑
        cls 是 User类的意思
        :param args:
        :param kwargs:
        """
        print("in new")
        return super().__new__(cls)

    def __init__(self, name):
        print("in init")
        self.name = name

    def get_name(self):
        return self.name


# new  是用来控制对象的生成过程，在对象生成之前
# init 是用来晚上对象的
# 如果new方法不返回对象，则不会调用init函数

if __name__ == "__main__":
    user = User(name="hsz")
    # 如果new方法不返回对象，则不会调用init函数
    # 只有 return super().__new__(cls)
    # 实例化对象的时候 才会调用 init



