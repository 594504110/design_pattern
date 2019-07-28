# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-28 20:56
@File    : 经典的单例模式.py
@Describe: 
"""
"""
单例模式的要求:
1. 只允许singleton类生成一个实例
2. 如果已经有一个实例了,我们需要重复提供一个对象
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    s1 = Singleton("wang")
    s2 = Singleton("liu")
    s3 = Singleton("zhang")
    s4 = Singleton("li")
    s5 = Singleton("zhao")
    print(s1, "\n", s2, "\n", s3, "\n", s4, "\n", s5)
    print(s1.name)
    print(s2.name)
    print(s3.name)
    print(s4.name)
    print(s5.name)
