#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
通过queue的方式进行线程间的同步

线程安全的
"""
from queue import Queue
import threading
import time


def get_detail_html(queue):
    """
    爬取文章详情页
    :param detail_url_list:
    :return:
    """
    # while True:
    url = queue.get()
    # 下面是爬取的逻辑
    print("get detail html data start ")
    # time.sleep(2)
    print("get detail html data end ")


def get_detail_url(queue):
    """
    爬取文章列表页
    :param queue:
    :return:
    """
    # while True:
    print("get_detail_url start")
    # time.sleep(4)
    for i in range(20):
        queue.put(i)
    print("get_detail_url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    url_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    url_thread.start()
    url_thread.join()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
        html_thread.join()

    detail_url_queue.task_done()
    detail_url_queue.join()

