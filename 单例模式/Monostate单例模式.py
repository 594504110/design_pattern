# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-28 21:18
@File    : Monostate单例模式.py
@Describe: 
"""
"""
这里讨论的事Gof编写的设计模式图书中提到的单例模式
一个类有且只有一个对象,然而根据Alex Martelli的说法,通常开发者需要的是让实例共享相同的状态,
他们建议开发者应该关注状态和行为,而不是同一性,由于概念基于所有对象共享的状态,因此被称为Monostate(单态)模式
"""


class Borg(object):
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


class SingletonBorg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(SingletonBorg, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    borg = Borg()
    borg.x = 4
    borg.y = 78
    # print(borg.__dict__)
    borg1 = Borg()
    # print(borg1.__dict__)

    s = SingletonBorg("wang")
    s1 = SingletonBorg("zhang")
    s2 = SingletonBorg("li")
    print(s.name)

