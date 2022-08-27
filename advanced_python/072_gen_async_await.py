#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
# 生成器是可以暂停的函数

1. 用同步的方式编写异步的代码，在适当的时候暂停函数并在适当的时候启动函数

tornado 是基于生成器协程实现的，不是async和await 的原生协程实现的
"""

import inspect


def gen_func():
    value = yield 1
    # 上面表示： 1. 返回值给调用方 2.调用方通过send方式返回值给gen
    return "hsz"


if __name__ == "__main__":
    gen = gen_func()
    # 获取生成器状态
    print(inspect.getgeneratorstate(gen))  # GEN_CREATED
    next(gen)
    print(inspect.getgeneratorstate(gen))  # GEN_SUSPENDED
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))  # GEN_CLOSED
