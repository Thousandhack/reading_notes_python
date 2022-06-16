#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
python的面向对象更加彻底
python的一切都是对象
类，函数，模块，库都是对象
类是可以实例化对象

类就相当于是一个模板对象

函数和类也是对象，属于python的一等公民：
    1.赋值给一个变量
    2.可以添加到集合对象中
    3.可以作为参数传递给函数
    4.可以做函数的返回值
"""


# 函数和类赋值变量的例子

def func_demo(name="xiao"):
    print(name)


class Person:
    def __init__(self):
        self.name = "hsz"
        print("=========", self.name)


demo = func_demo  # 将函数赋值给一个变量
# demo("two")

person = Person
# # 实例化对象
# person()


demo_list = []
demo_list.append(demo)
demo_list.append(person)

for item in demo_list:
    print(item())


def decorator_func():
    print("dec start")
    return func_demo


# 可以做函数的返回值
my_func = decorator_func()
my_func("tom")
