#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

from collections.abc import Mapping, MutableMapping
from collections.abc import __all__

# dict 属于 Mapping 类型


a = dict()
print(isinstance(a, MutableMapping))
