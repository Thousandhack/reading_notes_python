#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
我的这个实验中是打印不出来的
多进程编程
进程间的通信
通过pipe 实现进程通道
pipe 的性能是高于queue
"""
from multiprocessing import Process, Pipe


def producer(pipe):
    pipe.send("hello")


def consumer(pipe):
    print(pipe.recv())


if __name__ == "__main__":
    receive_pipe, send_pipe = Pipe()
    # pipe 只能使用与两个进程中的通信
    my_producer = Process(target=producer, args=(send_pipe,))
    my_producer.start()
    my_producer.join()
    my_consumer = Process(target=consumer, args=(receive_pipe,))

    my_consumer.start()

    my_consumer.join()
