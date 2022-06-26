#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import bisect

"""
用来处理已排序的序列，用来维持已排序的序列
"""

inter_list = []

bisect.insort(inter_list, 3)

bisect.insort(inter_list, 2)

bisect.insort(inter_list, 5)

bisect.insort(inter_list, 1)

bisect.insort(inter_list, 6)

print(inter_list)
# [1, 2, 3, 5, 6]

bisect.insort(inter_list, 3.0)
bisect.bisect_left(inter_list, 3)

print(inter_list)
