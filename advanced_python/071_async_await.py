#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
python 为了将语义变得更加明确，将引入了async 和 await 关键词 用于定义原生的协程

async 和 await 是配对的，不能和yield from 和 yield 一起使用

"""


async def download_loader(url):
    return "hsz"


# import types
#
# @types.coroutine
# def download_loader(url):
#     yield "hsz"

async def download_url(url):
    # do something
    html = await download_loader(url)
    # await 对比 yield from
    # download_loader(url) 是一个Awaitable对象
    return html


if __name__ == "__main__":
    ret = download_url("www.baidu.com")

    try:
        ret.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
