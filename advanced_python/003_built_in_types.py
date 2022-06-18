#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


"""
python 中的常见内置类型
对象的三个特征： 1.身份 2.类型 3.值

None （全局只有一个）
数值
迭代类型
序列类型  可以用for循环进行遍历
映射（dict）
集合  # set  frozenset （不可以修改的set）
上下文管理器类型  ( with )
其他
    模块类型
    class和实例
    函数类型
    方法类型
    代码类型
    object对象
    type类型
    ellipsis 类型（省略号）
    notimplemented 类对象

"""

a = None
b = None
print(id(a) == id(b))  # 说明None 全局只有一个


