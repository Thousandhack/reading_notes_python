#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
多进程编程
进程间通信
两个进程修改同一个变量
"""
from multiprocessing import Process, Pipe, Manager


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    process_dict = Manager().dict()
    first_process = Process(target=add_data, args=(process_dict, "hsz01", 22))
    second_process = Process(target=add_data, args=(process_dict, "hsz02", 23))

    first_process.start()
    second_process.start()

    first_process.join()
    second_process.join()
    print(process_dict)  # {'hsz01': 22, 'hsz02': 23}
