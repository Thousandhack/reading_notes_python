#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
多进程
# 耗cpu的操作，用多进程编程，对于io 操作来说，使用多线程编程，进程切换代价要高于线程

1.对于耗费cpu的操作，计算   多进程优于多线程

"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    # 1.下面就是一个耗cpu的操作，多进程优于多线程
    # 多线程demo
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("get {} ".format(data))
    #     end_time = int(time.time())
    #     print("last time is {}".format(end_time -start_time))

    # 多进程demo
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("get {} ".format(data))
    #     end_time = int(time.time())
    #     print("last time is {}".format(end_time -start_time))

    # 2.io操作多的时候，多线程优于多进程
    # 多线程demo
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 100]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("get {} ".format(data))
        end_time = int(time.time())
        print("last time is {}".format(end_time - start_time))

    # 多进程demo
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(random_sleep, (num)) for num in [2] * 100]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("get {} ".format(data))
    #     end_time = int(time.time())
    #     print("last time is {}".format(end_time -start_time))
