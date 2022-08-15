#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# import select
"""
使用非阻塞io 完成http请求

使用select完成http请求
DefaultSelector 在windows下是select ,在linux下就是epoll


通过非阻塞io实现http请求
# 并发性高
# 使用单线程
"""

selector = DefaultSelector()

urls = ["https://www.baidu.com"]
stop = False


class Fetcher:

    def __init__(self):
        self.host = ""
        self.path = ""
        # self.spider_url = ""
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = b""

    def recv_data(self, key):
        d = self.conn.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data.encode(encoding="utf8"), "1111")
            self.conn.close()
            # 兼容windows
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def connected(self, key):
        selector.unregister(key.fd)
        self.conn.send(
            "GET {} HTTP/1.1\r\nHost:{}"
            "\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.conn.fileno(), EVENT_READ, self.recv_data)

    def get_url(self, url):
        """
        通过socket请求html
        :param url:
        :return:
        """
        # 兼容windows
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == "":
            self.path = "/"
        # 建立socket连接
        self.conn.setblocking(False)
        try:
            self.conn.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册
        # 注册文件描述符  事件（读事件，写事件）  回调函数(只写函数名称)
        selector.register(self.conn.fileno(), EVENT_WRITE, self.connected)


def my_loop():
    """
    事件循环： 不停的请求socket的状态并调用对应的函数
    1.select 本身是不支持register模式的
    2.socket 状态变化的回调需要自己开发完成的

    :return:
    """

    while not stop:
        res_ = selector.select()
        print("===================res_",res_)
        for key, mask in res_:
            call_back = key.data
            call_back(key)

    # 回到+ 事件循环 + select(poll/epoll)


if __name__ == "__main__":
    fetcher = Fetcher()

    fetcher.get_url("https://www.baidu.com")

    ret  = my_loop()
    print("===================11111", ret)
