#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
线程变量同步

使用多线程的锁
1.用锁会影响性能
2.锁还会引起死锁
    （1）Lock不能多次调用acquire
    （1）RLock 多次调用acquire与release 数量不匹配(需要匹配)
    （2）a线程先用资源1再用并锁资源2 ，b 线程 先用资源2再用并锁资源1


web,电商网站开发（减少库存）
"""

from threading import Lock
# from threading import RLock
from threading import Thread
import time

total = 0
lock = Lock()


def add():
    global total
    global lock
    for i in range(10000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(10000000):
        """
        加锁
        与释放锁
        """
        lock.acquire()
        total -= 1
        lock.release()


thread_01 = Thread(target=add)

thread_02 = Thread(target=desc)

thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()

print(total)
