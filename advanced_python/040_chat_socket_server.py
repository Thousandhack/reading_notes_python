#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import socket
import threading

sk = socket.socket()
sk.bind(("127.0.0.1", 9900))

# 监听端口
sk.listen()


def handle_socket(conn, addr):
    while True:
        res = conn.recv(1024)
        # 把字节流编程原本字符串
        res2 = res.decode("utf-8")
        print("客户端说:", res2)
        content = input("服务器说:")
        conn.send(content.encode("utf-8"))
        if content == "q":
            break
    # 执行四次挥手
    conn.close()


while True:
    # 建立三次握手
    conn, addr = sk.accept()
    # 用线程处理新接收的连接
    # target 一定是函数的名称
    conn_thread = threading.Thread(target=handle_socket, args=(conn, addr))
    # 启动线程
    conn_thread.start()
# 退出系统端口
sk.close()
