#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
yield from 的原理
pep 380

# 1.RESULT = yield from EXPR 可以简化成下面这样
# 一些说明
_i : 子生成器，同事也说一个迭代器
_y : 子生成器生产的值
_r: yield from 表达式最终的值
_s: 调用方通过send() 发送的值
_e: 异常对象

"""
import sys

"""
以下就是处理StopIteration的代码逻辑的一个demo
"""
# _i = iter(EXPR)  # EXPR 是一个可迭代对象，_i 其实是子生成器
# try:
#     _y = next(_i)   # 预激子生成器，把产出的第一个值存在_y 中
# except StopIteration as _e:
#     _r = _e.value    # 如果抛出StopIteration异常，那么就将异常对象的value
# else:
#     while True:       # 尝试执行这个循环，委托生成器会阻塞
#         _s = yield _y   # 生产子生成器的值，等到调用方send() 的值，发送过来的的值报存在_s 中
#         try:
#             _y = _i.send(_s)      # 转发_s, 并尝试向下执行
#         except StopIteration as _e:
#             _r = _e.value   # 如果子生成器抛出异常， 那么就获取异常对象的
#             break
#
# RESULT = _r      # _r 就是整个yield from 表达式返回的值


"""
1.子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以它不支持.throw() 和 .close() 方法
2.如果子生成器支持.throw() 和 .close() 方法，但是在子生成器内部，这两个方法都会抛异常；
3.调用方让子生成器自己抛出异常
4.当调用方使用next() 或者.send(None)时，都要在子生成器上调用next() 函数，当调用使用.send() 发送非None值时，才调用子生成器的.send()方法

以下为完整的yield from 的逻辑：

_i = iter(EXPR)  # EXPR 是一个可迭代对象，_i 其实是子生成器
try:
    _y = next(_i)   # 预激子生成器，把产出的第一个值存在_y 中
except StopIteration as _e:
    _r = _e.value    # 如果抛出StopIteration异常，那么就将异常对象的value
else:
    while True:       # 尝试执行这个循环，委托生成器会阻塞
        _s = yield _y   # 生产子生成器的值，等到调用方send() 的值，发送过来的的值报存在_s 中
        try:
            _y = _i.send(_s)      # 转发_s, 并尝试向下执行
        except StopIteration as _e:
            _r = _e.value   # 如果子生成器抛出异常， 那么就获取异常对象的
            break

RESULT = _r      # _r 就是整个yield from 表达式返回的值

"""
# _i = iter(EXPR)  # EXPR 是一个可迭代对象，_i 其实是子生成器
# try:
#     _y = next(_i)   # 预激子生成器，把产出的第一个值存在_y 中
# except StopIteration as _e:
#     _r = _e.value    # 如果抛出StopIteration异常，那么就将异常对象的value
# else:
#     while True:       # 尝试执行这个循环，委托生成器会阻塞
#         try:
#             _s = yield _y   # 生产子生成器的值，等到调用方send() 的值，发送过来的的值报存在_s 中
#         except GeneratorExit as _e:
#             try:
#                 _m = _i.close
#             except AttributeError:
#                 pass
#             else:
#                 _m()
#             raise _e
#         except BaseException as _e:
#             _x = sys.exc_info()
#             try:
#                 _m = _i.throw
#             except AttributeError:
#                 raise _e
# RESULT = _r      # _r 就是整个yield from 表达式返回的值

"""
总结如下：
1.子生成器生产的值，都是直接传给调用方的；调用方通过.send() 发送的值都是直接传递给子生成器的；
如果发送的是None,会调用子生成器的__next__ 方法，如果不是None会调用子生成器的.send()方法；
2.子生成器退出的时候，最后的return EXPR,会触发一个StopIteration（EXPR）异常；
3.yield from 表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
4.如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同事其他的异常会向上“冒泡”；
5.传入委托生产器的异常里,除了GeneratorExit之外,其他的所有异常全部传递给子生成器.throw()方法；
如果调用.throw()的时候出现了StopIteration异常，那么就恢复委托生成器的运行，其他的异常全部向上“冒泡”
6.如果在委托生成器上调用.close() 或传入GeneratorExit 异常，会调用子生成器的.close() 方法，没有的话就不调用。
如果在调用.close() 的时候抛出了异常，那么向上“冒泡”，否则的话委托生成器会抛出 GeneratorExit 异常



"""


