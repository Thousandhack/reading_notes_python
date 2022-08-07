#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

from concurrent import futures

"""
from concurrent import futures
主要用于进程池和线程池编程的

# 线程池  为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候，我们主线程能立即知道
# futures 可以让多线程和多进程编码接口一致

管理线程池
"""
from concurrent.futures import ThreadPoolExecutor
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)
# submit 立即返回，非阻塞的
# task_01 和 # task_02 都是属于futures 的类方法
task_01 = executor.submit(get_html, (3))
task_02 = executor.submit(get_html, (2))
# 通过submit函数提交执行的函数到线程池中

# done 用于判断某个任务是否完成
print(task_01.done())

# 当线程池小于任务数量且不是第一个任务才能被cancel
# 否则开始执行的任务和执行结束的任务都不能cancel
print(task_02.cancel())

# 执行的返回结果
# result 获取task的执行结果
ret = task_01.result()
print(ret)
