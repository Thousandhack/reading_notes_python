#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
gil global interpreter lock (cpython)
python 中一个线程对应于C语言中的一个线程
gil 使得同一个时刻只有一个线程在一个cpu上执行字节码
无法将多个线程映射到多个cpu上 ，并发在某个程度上受限

gil 是会释放的，gil并不是一个线程执行完才释放的

gil 什么时候释放？
gil 会根据执行的字节码行数以及时间片释放gil
gil 遇到io的操作的时候主动释放

"""

# import dis
#
# def add(a):
#     a = a +1
#     return a
# print(dis.dis(add))

import threading

total = 0


def add():
    global total
    for i in range(10000000):
        total += 1


def desc():
    global total
    for i in range(10000000):
        total -= 1


thread_01 = threading.Thread(target=add)

thread_02 = threading.Thread(target=desc)

thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()


print(total)