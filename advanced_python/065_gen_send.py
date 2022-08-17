#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
协程介绍之 从生成器开始


"""


def gen_func():
    # 下面的一行代码的作用为：
    # 1.产出值  2.可以接收值（调用方传递进来的值）
    html = yield "www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "hsz"

# 1. 生成器不只，可以产出值，还可以接收值



if __name__ == "__main__":
    gen = gen_func()
    # 1. 启动生成器有两种 next() , send
    # （1）方式一
    # url = next(gen)
    # （2）方式二 ： 必须 是None
    gen.send(None)
    # 模拟download url
    zz = "hsz"
    # gen.send(zz)  # send方法可以传递值进入生成器内部，同时还可以重启执行到下一个yield的位置
    print(gen.send(zz))  # 注释上面一行改为打印这个send ，打印结果为 2

    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))  没有yield 的话会报错
