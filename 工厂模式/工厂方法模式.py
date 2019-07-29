# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-29 22:47
@File    : 工厂方法模式.py
@Describe: 
"""
from abc import ABCMeta, abstractmethod

# 以下几点可以帮助我们了解工厂方法模式
"""
1. 我们定义了一个接口，但是工厂本身并不负责创建对象，而是将这一任务交给子类来完成，即子类决定了要实现那些类
2. Factory方法的创建是通过继承而不是实例化来完成的
3. 工厂方法使设计更加具有可定制性，他可以返回相同的实例或子类，而不是某种类型的对象(就想在简单工厂模式中那样简单)
"""

# 工厂方法模式的优点
"""
1. 他具有更大的灵活性，是的代码更加的通用，因为他不单纯的实例化某一个类，这样实现那些类取决于接口，而不是类
2. 他们是松耦合的，因为创建对象的代码与使用对象的代码是分开的，客户端完全不需要关心要传递那些参数以及要实例化那些类，
由于添加新类更加容易，所以降低了维护的成本。
"""


# 通过某个子类的某个方法创建不同的实例或多个不同的实例
# 创建怎样的实例，取决于调用的那些子类的实现方法如何。


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonSection(Section):

    def describe(self):
        print("Person Section")


class AlbumSection(Section):

    def describe(self):
        print("Album Section")


class PatentSection(Section):

    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.section = []

    @abstractmethod
    def create_profile(self):
        pass

    def get_section(self):
        return self.section

    def add_section(self, section):
        self.section.append(section)


class Linked(Profile):
    def create_profile(self):
        self.add_section(PersonSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class FaceBook(Profile):
    def create_profile(self):
        self.add_section(PersonSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    profile_type = input("type: ")
    profile = eval(profile_type)()
    profile.create_profile()
    print(profile.get_section())
