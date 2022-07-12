#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz
import numbers


class IntField:

    def __init__(self, min=None, max=None):
        self._value = None
        self.min = min
        self.max = max
        if min is not None:
            if isinstance(min, numbers.Integral):
                raise ValueError("min value must be int")

            elif min < 0:
                raise ValueError("min muse be positive int")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self._value = value


class CharField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value


class User:
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", min=0, max=100)

    class Meta:
        db_table = "user"


if __name__ == "__main__":
    user = User()
    user.name = "hsz"
    user.age = 28
    user.save()
