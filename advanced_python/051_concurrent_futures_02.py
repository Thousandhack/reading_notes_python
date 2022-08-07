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
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
#

time_list = [3, 2, 4]

"""
获取多线程中执行后的结果的返回值
"""

# 法一：
# 要获取已经成功的task的返回
# all_task = [executor.submit(get_html,(times)) for times in time_list ]
# for future in as_completed(all_task):
#     data = future.result()
#     print("get return  {} page success".format(data))


# 法二:
# 通过executor的map 获取已经完成的task的值
# for data in executor.map(get_html, time_list):
#     print("get return  {} page success".format(data))


#  wait的使用
all_task = [executor.submit(get_html, (times)) for times in time_list]
# 默认可以等到所有执行完才继续执行
# 设置FIRST_COMPLETED 表示第一个执行完后就会继续执行main
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
