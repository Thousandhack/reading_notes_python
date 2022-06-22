#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
类方法，静态方法，实例方法
"""


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12] and self.day == 31:
            self.month += 1
            self.day = 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        elif self.month in [4, 6, 9, 11] and self.day == 30:
            self.month += 1
            self.day = 1
        elif self.month == 2 and self.day >= 28:
            if self.year % 3 == 0 and self.day == 28:
                self.day += 1
            else:
                self.month += 1
                self.day = 1

        else:
            self.day += 1

    @staticmethod
    def parse_from_str(date_str):
        """
        静态方法
        :param date_str:
        :return:
        """
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        """
        类方法
        :param date_str:
        :return:
        """
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":

    new_day = Date(2020,12,31)
    new_day.tomorrow()
    print(new_day)

    data_str = "2020-12-31"
    # 用staticmethod完成初始化
    new_day = Date.parse_from_str(data_str)
    new_day.tomorrow()
    print(new_day)

    # 用 classmethod 完成初始化
    new_day = Date.from_string(data_str)
    new_day.tomorrow()
    print(new_day)
