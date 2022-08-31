#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
包含各种特定系统实现的模块化事件循环
传输和协议抽象

对TCP、UDP、SSL、子进程、延时调用以及其他的具体支持

模仿futures 模块但适用于事件循环使用的Future类

基于yield from 的协议和任务，可以让你用顺序的方式编码并发代码

必须使用一个将产生阻塞IO的调用时，有接口可以把这个事件转义到线程池

模仿threading模块中的同步原语、可以用在单线程内的协程之间


协程编码模型三个条件：
事件循环 + 回调（驱动生成器） + epoll[IO多路复用]
asyncio 是python 用于解决异步io编程的一套解决框架

tornado 、gevent、twisted( scrapy, django channels)
tornado  实现web服务,可以直接部署 + nginx
django + flask 本身不提供服务器，需要搭配 uwsgi,gunicorn + nginx

以下为一个最简单的协程的demo 和 多任务协程的demo
"""

# 使用asyncio

import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 只有一个的情况
    # loop.run_until_complete(get_html("www.baidu.com"))
    # 有很多任务的情况
    tasks = [get_html("www.baidu.com") for _ in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
    """
    TypeError: object NoneType can't be used in 'await' expression
    因为await 后面调用的方法返回None
    """
