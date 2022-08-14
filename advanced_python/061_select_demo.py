#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import socket
from urllib.parse import urlparse

"""
使用非阻塞io 完成http
"""


def get_url(url):
    """
    通过socket请求html
    :param url:
    :return:
    """
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setblocking(False)
    try:
        conn.connect((host, 80))
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好，需要while循环不断的去检查状态
    # 做计算任务或者再次发起其他的连接请求
    while True:
        try:
            conn.send(
                "GET {} HTTP/1.1\r\nHost:{}"
                "\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass
    data = b""
    while True:
        try:
            d = conn.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data.encode(encoding="utf8"), "1111")
    conn.close()


if __name__ == "__main__":
    get_url("https://www.baidu.com")
