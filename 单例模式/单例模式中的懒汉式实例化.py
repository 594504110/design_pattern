# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-28 21:08
@File    : 单例模式中的懒汉式实例化.py
@Describe: 
"""
"""
单例模式的用例之一就是懒汉式实例化
例如:在导入模块的时候,我们可能会无意中创建一个对象,但是当时根本用不到
懒汉式实例化能够确保只有在使用的时候才会创建对象
所以,懒汉式实例化是一种节约资源并且仅在需要的时候才会创建的一种单例模式
"""


class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == '__main__':
    s = Singleton()
    s = Singleton.get_instance()
    print(s)
