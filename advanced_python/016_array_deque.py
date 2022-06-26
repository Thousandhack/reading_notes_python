#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
array ,deque


布隆过利器

"""
# array
import array

array_demo = array.array("i")

array_demo.append(1)
array_demo.append(22)
print(array_demo)
print(array_demo[0])

array_demo_01 = array.array("f")

array_demo_01.append(1.66)
array_demo_01.append(2.33)
print(array_demo_01)
print(array_demo_01[0])
