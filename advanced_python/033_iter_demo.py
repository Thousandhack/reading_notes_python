#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
python中的迭代协议

什么是迭代协议
迭代器是什么
    迭代器是访问集合内元素的一种形式，一般用来遍历数据

迭代器和以下标的访问方式不一样，迭代器是不能返回的，
迭代器提供了一种惰性访问数据的方式


Iterable    可迭代
Iterator    迭代器

"""

from collections.abc import Iterable, Iterator

a = [1, 2]

# 列表是可迭代的，但是不是一个迭代器
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
