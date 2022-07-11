#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
自定义元类

什么是元类
    元类是创建类的类   对象 <- class <- type


#类也是对象，type是创建类的类

"""


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


def say(self):
    return "hello hsz"


class BaseClass:
    def answer(self):
        return "I am baseclass"


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


# 元类来创建
class Student(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "student"


# python中类的实例化过程
# type 去创建类对象，
# 如果有元类，会首先寻找metaclass,通过metaclass去创建user类


if __name__ == "__main__":
    MyClass = create_class("user")
    """
    动态创建类
    """

    # print(MyClass)
    # my_object = MyClass()
    # print(my_object)

    # 使用type创建类

    User = type("User", (BaseClass,), {"name": "hsz", "say": say})
    object = User()
    print(object.name)
    print(object.say())
    print(object.answer())

    stu = Student(name="lin")
    print(stu)

