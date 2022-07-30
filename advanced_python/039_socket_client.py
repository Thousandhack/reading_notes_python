#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
socket 客户端
"""

import socket

# 产生一个socket对象
server = socket.socket()

server.connect(("127.0.0.1", 9000))

# 发送消息
server.send("你好".encode("utf-8"))

# 接收消息
res = server.recv(1024)
str_var = res.decode("utf-8")
print(str_var)
server.close()
