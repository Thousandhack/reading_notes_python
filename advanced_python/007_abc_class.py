#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
抽象基类 （abc模块）
在基础的类，设定一些方法
抽象基类无法实例化的

两种应用场景
1.检查一个类是否有某种方法
2.需要强制某个子类必须实现某些方法的规定
"""


class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby", "hsz"])
# hasattr 判断一个类是否有某种方法
# print(hasattr(com, "__len__"))

# 这个是一个抽象基类
# 所有的抽象基类，所有的matacalss 他们的类都是ABCMeta

from collections.abc import Sized

# 在某些情况下之下希望某个对象的类型
print(isinstance(com, Sized))

# 我们需要强制某个子类必须实现某些方法

# 版本1 : 实例化调用相应的方法再报错
# 如何去模拟一个抽象基类
# 基类的方法，子类一定实现相应的方法，否则调用对应的方法就会报错
# class CacheBase():
#
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#
#     def set(self, key, value):
#         pass
#
#
# redis_cache = RedisCache()
# redis_cache.set("key", "value")

# 版本2: 直接使用类的时候就报错
import abc


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod  # abc 的抽象方法
    def get(self, key):
        """
        这边可以直接pass ,如果子类没有对应的方法，实例化的时候就会报错
        :param key:
        :return:
        """
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    """
    子类继承 基类的话，对于的方法一定要实现，不然直接报错
    下面的方法只有随便注释一个直接报错
    """

    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis_cache = RedisCache()
