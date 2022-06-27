#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

# 不建议继承list和dict
from collections import UserDict
class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
my_dict["one"] = 1
print(my_dict)

from collections import defaultdict

dict_demo = defaultdict(dict)
dict_value = my_dict["name"]

print(dict_value)


