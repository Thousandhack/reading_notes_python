#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz
import os
import time

"""
多进程编程
"""
# fork 只能用于linux 下
# fork 表示创建子进程
pid = os.fork()
# pid 会返回两次，一次是子进程，一次是父进程
print("============")  # 会打印两次
if pid == 0:
    print("子进程 {}，父进程：{}".format(os.getgid(),os.getppid()))
else:
    print("我是父进程：{}".format(pid))

time.sleep(2)