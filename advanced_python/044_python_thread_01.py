#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
对于io操作来说，多线程和多进程性能差别不大，甚至多线程比多进程性能还高
python 多线程
1. 通过Thread类实例化
"""
import threading
import time


def get_detail_html(url):
    print("get detail html data start ")

    time.sleep(2)
    print("get detail html data end ")


def get_detail_url(url):
    print("get_detail_url start")
    time.sleep(4)
    print("get_detail_url end")


if __name__ == "__main__":
    thread_01 = threading.Thread(target=get_detail_html, args=("",))
    thread_02 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()
    # 守护线程
    # thread_01.setDaemon(True)
    # thread_02.setDaemon(True)
    thread_01.start()
    thread_02.start()

    # 等到两个线程执行完成才执行后面的主线程
    thread_01.join()
    thread_02.join()
    # 当主线程退出的时候，子线程kill掉
    print("last time:{}".format(time.time()- start_time))