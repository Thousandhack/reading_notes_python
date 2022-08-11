#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
多进程编程
队列

全局变量不使用于多进程编程，可适用于多线程
"""
import time
from multiprocessing import Process, Queue, Pool
from multiprocessing import Manager


def producer(a):
    a += 1
    time.sleep(2)


def consumer(a):
    time.sleep(2)
    print("a={}".format(a))


if __name__ == "__main__":
    a = 1
    my_producer = Process(target=producer, args=(a,))
    my_consumer = Process(target=consumer, args=(a,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
    # 运行结果打印： a=1
