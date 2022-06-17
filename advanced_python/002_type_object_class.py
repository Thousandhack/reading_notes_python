#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
type 有两个作用：1. 返回一个变量的数据类型  2.通过type生成一个类
type 是一个类，同时type也是一个对象
object  是所有类都要继承的顶层的基类

object 是 type的一个实例，type创建了所有对象
type 继承了object ,type也是自己的对象
所以也就是一切的类都是继承了object

为什么说python一切皆对象:
所以的对象都是由type生成的，所以一切皆对象。
"""

a = 1
print(type(a))  # int 类型
print(type(int))  # type 类型


# 通过type 生成int 通过 int 生成 1
# type -> int -> 1

class Student:
    pass


stu = Student()

print(type(stu))  # __main__.Student
print(type(Student))  # type
print(Student.__base__)  # object
# 通过 type生成 class 通过 class 生成 obj
# type -> class -> object

print(Student.__bases__)  # 打印这个类的所有基类

print(type.__bases__)  # object type 的基类是object
print(type(object))  # type   object是由type生成
print(object.__bases__)  # ()   object 的基类是空
