# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-28 21:36
@File    : 单例和元类.py
@Describe: 
"""


class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("this is MyInt")

        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__()
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == '__main__':
    i = int(3, 4)
    l1 = Logger()
    l2 = Logger()
    print(l1, l2)
