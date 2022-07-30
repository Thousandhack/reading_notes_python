#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
socket 服务端
"""

import socket

# 创建一个socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口(注册网络,让客户端可以找到你)
# #'127.0.0.1" 默认本机的ip
server.bind(("127.0.0.1", 9000))

# 开始监听
server.listen()

# 建立三次握手,建立连接,程序加了阻塞
# 建立三次握手如果失败,程序不往下执行
# 接受客户端的连接请求
conn, addr = server.accept()
print(conn, addr)

# 设置最大一次性接收1024字节,程序再次加上阻塞,没有接收到数据,不会向下执行代码
msg = conn.recv(1024)

# 把字节流恢复成正常的字符串
print(msg.decode("utf-8"))

# 发送给客户端数据,发送前需要把数据编码成二进制字节流
conn.send("你也好呀".encode("utf-8"))

# 执行四次挥手,断开连接
conn.close()

#  传输完毕后，关闭套接字,退还占用的端口
server.close()
