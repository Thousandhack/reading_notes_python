#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


a = {
    "user_info": {
        "name": "hsz",
        "age": 10
    }
}

# 更新字典的键对应的值
b = a.setdefault("address_info", "shenzhen")

print(a)
print(b)

#
a.update(address_info="fujian")

print(a)