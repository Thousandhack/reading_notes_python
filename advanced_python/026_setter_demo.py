#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
在python内置的装饰器中，@property和@XXX.setter是针对于getter和setter方法的不二之选。
    当一个方法（函数）的最终目的是返回一个值时，可以@property装饰该方法，这样就可以达成getter方法。
    当在一个方法的上方使用XXX.setter装饰时，代表可以直接通过类实例对象名称.变量名为其变量赋值，其中XXX代表变量名同时也是方法（函数）名称
"""


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
# 获取商品价格
print(obj.price)
# 修改商品原价
obj.price = 200
print(obj.price)
del obj.price  # 删除商品原价
