# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-29 23:26
@File    : 抽象工厂模式.py
@Describe:
"""
from abc import ABCMeta, abstractmethod

"""
抽象工厂模式的主要目的是提供一个接口来创建一系列相关对象，而无需指定具体的类，
工厂方法将创建实例的任务委托给了子类，而抽象工厂方法的目标是创建一系列相关的对象
"""


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    """
    印度披萨
    """

    def create_veg_pizza(self):
        return DeluxeVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class UspVegPizza(PizzaFactory):
    """
    美式披萨
    """

    def create_veg_pizza(self):
        return MexcanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    """
    蔬菜披萨
    """

    @abstractmethod
    def prepare(self):
        """
        准备

        :return:
        """
        pass


class NonVegPizza(metaclass=ABCMeta):
    """
    非蔬菜披萨
    """

    @abstractmethod
    def serve(self, veg_pizza):
        """
        提供

        :param veg_pizza:
        :return:
        """
        pass


class DeluxeVeggiePizza(VegPizza):

    def prepare(self):
        print("prepare", type(self).__name__)


class ChickenPizza(NonVegPizza):

    def serve(self, veg_pizza):
        print(type(self).__name__, "is served with chicken on ", type(veg_pizza).__name__)


class MexcanVegPizza(VegPizza):

    def prepare(self):
        print("prepare", type(self).__name__)


class HamPizza(NonVegPizza):

    def serve(self, veg_pizza):
        print(type(self).__name__, "is served with Ham on ", type(veg_pizza).__name__)


class PizzaStore:

    def __init__(self):
        self.factory = None
        self.non_veg_pizza = None
        self.veg_pizza = None

    def make_pizza(self):
        for factory in [IndianPizzaFactory(), UspVegPizza()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizza()

"""
工厂方法：
1. 他向客户端开放一个创建对象的方法
2. 他使用继承和子类决定要创建那个对象
3. 工厂方法用于创建一个产品

抽象工厂方法:
1. 抽象工厂方法包含一个或多个工厂方法来创建一个系列的相关对象。
2. 他使用组合将创建对象的任务委托给其他类
3. 抽象工厂方法用于创建相关产品的系列
"""
