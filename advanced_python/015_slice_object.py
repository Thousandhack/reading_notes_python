#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass



if __name__ == "__main__":
    group = Group(company_name="")