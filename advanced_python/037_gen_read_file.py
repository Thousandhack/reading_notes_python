#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


"""
生成器如何读取大文件


背景：一行500G的文件
"""


def my_read_lines(f, new_line):
    buf = ""
    while True:
        while new_line in buf:
            pos = buf.index(new_line)
            yield buf[:pos]
            buf = buf[pos + len(new_line):]
        # 一次性读取的量
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk


with open("read_demo") as f:
    # 第一个参数为文件的句柄 第二个参数为分隔符
    for line in my_read_lines(f, "{|}"):
        print(line)

