#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
协程介绍之 从生成器开始


"""


def gen_func():
    # 下面的一行代码的作用为：
    # 1.产出值  2.可以接收值（调用方传递进来的值）
    try:
        html = yield "www.baidu.com"
        print(html)
    except Exception:
        pass

    yield 2
    yield 3
    return "hsz"

# 1. 生成器不只，可以产出值，还可以接收值



if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    # except GeneratorExit: # 会报下面的错误
    # RuntimeError: generator ignored GeneratorExit
    gen.close()  # gen.close() 就不能再next进行调用了
    # next(gen)
