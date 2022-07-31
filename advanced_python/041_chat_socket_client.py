#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9900))

while True:
    content = input("客户端说:")
    #发送的二进制字节流数据,所以都需要先编码
    sk.send(content.encode("utf-8"))
    res = sk.recv(1024).decode("utf-8")
    if res == "q":
        break
    print("服务端说:",res)

# 关闭连接
sk.close()