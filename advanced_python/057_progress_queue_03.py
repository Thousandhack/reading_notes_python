#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
多进程编程
队列
#  multiprocessing 中queue不能用于pool进程池
# pool 进程中的通信需要使用Manager中的Queue
全局变量不使用于多进程编程，可适用于多线程
"""
from multiprocessing import Manager, Pool
import time


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    # 什么打印没有
    # 可能版本问题Manager
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()
