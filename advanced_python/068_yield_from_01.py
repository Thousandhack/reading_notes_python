#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
生成器 yield from
python3.3 新加的


"""
from itertools import chain


def the_chain_demo():
    my_list = [1, 2, 3]
    my_dict = {
        "hsz_01": "www.baidu.com",
        "hsz_02": "www.huya.com"
    }
    for value in chain(my_list, my_dict):
        print(value)


def my_chain(*args, **kwargs):
    for iterable in args:
        yield from iterable
        # for value in iterable:
        #     yield value


# yield from iterable  # iterable 可迭代的对象
def my_chain_demo():
    my_list = [1, 2, 3]
    my_dict = {
        "hsz_01": "www.baidu.com",
        "hsz_02": "www.huya.com"
    }
    for value in my_chain(my_list, my_dict):
        print(value)


# ======================================

def gen_demo_01(iterable):
    yield iterable


def gen_demo_02(iterable):
    yield from iterable

#=============

def g1(gen):
    yield from gen

def main():
    """
    :return:
    """
    g = g1()
    g.send(None)

# 1. main 为调用方  g1 为委托生成器 gen 子生成器
# yield from 会在调用方与子生成器之间建立一个双向通道




##################

if __name__ == "__main__":
    # the_chain_demo()
    # my_chain_demo()

    # =======
    for value in gen_demo_01(range(10)):
        print(value)

    for value in gen_demo_02(range(10)):
        print(value)

