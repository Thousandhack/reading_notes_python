#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz
import os
import time

"""
多进程编程
"""
import multiprocessing


def get_html(n):
    print("sub process start")
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # # progress.daemon = True
    # progress.start()
    # print(progress.pid)
    # progress.join(2)
    # print("main progress end")

    # 使用进程池
    # 如果不指定进程池数量就是计算机多少个cpu就多少个进程
    pool = multiprocessing.Pool(3)
    result = pool.apply_async(get_html, args=(2,))

    # 等待所有任务完成
    pool.close()
    pool.join()
    print("result===={}".format(result.get()))

    # imap  通过方法不同线程返回不同结果
    # for ret in pool.imap(get_html, [1,5,3]):
    #     print("ret===",ret)

    # for ret in pool.imap_unordered(get_html, [1,5,3]):
    #     print("ret===",ret)