#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
生成器函数： 函数里只要有yield 关键字

生成器函数的实现

"""


def gen_func():
    yield 1


# 惰性求值和延迟求值提供了可能


def fib(index):
    """
    斐波那契
    :param index:
    :return:
    """
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)



def fib2(index):
    """
    斐波那契的实现过程
    :param index:
    :return:
    """
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


def fib_gen(index):
    """
    使用生成器 斐波那契的实现过程
    :param index:
    :return:
    """
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


def func():
    return 1


if __name__ == "__main__":
    # 返回生成器对象：python 编译字节码的时候就产生了
    gen = gen_func()
    print(gen)
    for value in gen:
        print(value)

    re = func()
    print(re)

    print(fib2(10))

    for value in fib_gen(10):
        print(value)
