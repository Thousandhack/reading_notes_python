#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz
import numbers
from datetime import date
from datetime import datetime


class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        """
        对参数类型的检查
        :param instance:
        :param value:
        :return:
        """
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        self.value = value


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class UserModel:
    age = IntField()


"""
如果user是某个类的实例， 那么user.age(以及等价的getattr(user,'age') )
首先调用__getattribute__ 。 如果类定义了 __getattr__ 方法
那么在 __getattribute__抛出 AttributeError 的时候就会调用到__getattr__,
而对于描述（__get__）的调用，则发生在 __getattribute__ 内部的。
user = User(),那么user.age 顺序如下：
（1）如果"age"是出现在User 或其基类的__dict__ 中， 且age是data descriptor,那么调用其__get__方法，否则
（2）如果"age" 出现在obj（user对象）的__dict__中，那么直接返回 obj.__dict__['age'],否则
（3）如果"age"出现在User或其基类的__dict__中
（3.1）如果age是non-data descriptor，那么调用其__get__方法，否则
（3.2）返回__dict__["age"]
（4） 如果User有__getattr__方法，调用__getattr__方法，否则
（5）抛出 AttributeError
"""

if __name__ == "__main__":
    user = UserModel()
    user.__dict__['age'] = "abc"
    print(user.__dict__)
    # print(user.age) # AttributeError: 'IntField' object has no attribute 'value'
    print(user.__dict__['age'])  # 和上面一行有区别的
