#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


"""
鸭子类型
多个类实现了相同的方法，只需要实现一个方法，然后多个类实例化后调用这个相同的方法
"""


class Cat(object):
    def say(self):
        print("I'm a cat")


class Dog(object):
    def say(self):
        print("I'm a dog")


class Duck(object):
    def say(self):
        print("I'm a duck")


def in_the_forest(animal):
    animal.say()


cat = Cat()
dog = Dog()
duck = Duck()
for x in [cat, dog, duck]:
    in_the_forest(x)
