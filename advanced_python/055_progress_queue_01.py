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

def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
    # 运行结果打印了 a


# 不知道为什么这个连 a 都没有打印
# def producer(a):
#     a += 1
#     time.sleep(2)
#
#
# def consumer(a):
#     time.sleep(2)
#     print("a={}".format(a))
#
#
# if __name__ == "__main__":
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


#  multiprocessing 中queue不能用于pool进程池
# pool 进程中的通信需要使用Manager中的Queue

def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    # 打印了a
    # 可能版本问题Manager
    queue = Manager().Queue(10)
    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()

