#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

import socket
from urllib.parse import urlparse

"""
requests -> urlib -> socket
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
    conn.connect((host, 80))

    conn.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    data = b""
    while True:
        d = conn.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print("html_data=", html_data.encode(encoding="utf8"))
    conn.close()


if __name__ == "__main__":
    get_url("https://www.baidu.com")
