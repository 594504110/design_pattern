# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-29 22:39
@File    : 简单工厂模式.py
@Describe: 
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):

    def do_say(self):
        print("wang wang wang ...")


class Cat(Animal):
    def do_say(self):
        print("miao miao miao ...")


class ForestFactory(object):
    """
    工厂类
    """

    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    # 客户端调用
    ff = ForestFactory()
    animal = input("Dog or Cat? :")
    ff.make_sound(animal)
