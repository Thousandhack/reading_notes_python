#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
协程介绍之 从生成器开始gen throw


"""


def gen_func():
    # 下面的一行代码的作用为：
    # 1.产出值  2.可以接收值（调用方传递进来的值）
    try:
        html = yield "www.baidu.com"
    except Exception:
        pass
    # print(html)
    yield 2
    yield 3
    return "hsz"


# 1. 生成器不只，可以产出值，还可以接收值


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "down error")  # 异常是前一个yield的异常,上面相应的方法里面加了try except 就不会抛出异常
    print(next(gen))
