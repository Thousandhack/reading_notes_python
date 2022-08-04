#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
线程间的通信

python 多线程
这个案例可以用来写爬虫
"""
import threading
import time


def get_detail_html(detail_url_list):
    """
    爬取文章详情页
    :param detail_url_list:
    :return:
    """
    # while True:
    if detail_url_list:
        url = detail_url_list.pop()
        # 下面是爬取的逻辑
        print("get detail html data start ")
        # time.sleep(2)
        print("get detail html data end ")


def get_detail_url(detail_url_list):
    """
    爬取文章列表页
    :param detail_url_list:
    :return:
    """
    # while True:
    print("get_detail_url start")
    # time.sleep(4)
    for i in range(20):
        detail_url_list.append(i)
    print("get_detail_url end")


# 线程间的通信方式
# 1.共享变量

if __name__ == "__main__":
    detail_url_list = []
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    thread_detail_url.start()
    thread_detail_url.join()
    print(detail_url_list)
    # for i in range(10):
    #     html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
    #     html_thread.start()
    #     html_thread.join()
    #
    #
    start_time = time.time()

    # 当主线程退出的时候，子线程kill掉
    print("last time:{}".format(time.time() - start_time))
