# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei
@Time    : 2019-04-27 16:05
@Software: PyCharm
@File    : 0.py
"""
"""
先天的原因并不能如意，
这时就需要通过服装、化妆去弥补。
所谓美女，
三分靠长相七分靠打扮！
比如身高不够，就可以通过穿高跟鞋来弥补；
如果本身就比较高，那穿不穿高跟鞋就没那么重要了。
这里的高跟鞋就起着一个适配的作用，
能让你的形象增高四、五厘米，
下面我们就用代码来模拟一下高跟鞋在生活中的场景吧
"""


class BasePerson:
    """
    接口基类，提供空实现的方法，由子类去实现
    """

    def get_name(self):
        """
        获取姓名
        :return:
        """

    def get_height(self):
        """
        获取身高
        :return:
        """


class HeightPerson(BasePerson):
    """
    个子高的人
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_height(self):
        return 170


class ShortPerson(BasePerson):
    """
    个子矮的人
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def get_real_height():
        """
        真实身高
        :return:
        """
        return 160

    @staticmethod
    def get_shoes_height():
        """
        鞋子的高度
        :return:
        """
        return 6


class DecoratePerson(ShortPerson, BasePerson):
    """
    装饰过得人，也就是传高跟鞋的人
    """

    def get_height(self):
        return super().get_real_height() + super().get_shoes_height()


def can_play_receptionist(_person):
    """
    判断一个人是否可以成为高级酒店接待员
    :param _person: 一个人
    :return:
    """
    return _person.get_height() >= 165


def person():
    """
    用来测试的人
    :return:
    """
    lisa = HeightPerson('lisa')
    print(f"姓名：{lisa.get_name()} - 身高：{lisa.get_height()}")
    print(f"是否适合做接待员：{'符合' if can_play_receptionist(lisa) else '不符合'}")
    print("-" * 20)
    eric = DecoratePerson("eric")
    print(f"姓名：{eric.get_name()} - 身高：{eric.get_height()}「在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！」")
    print(f"是否适合做接待员：{'符合' if can_play_receptionist(lisa) else '不符合'}")


person()
"""
姓名：lisa - 身高：170
是否适合做接待员：符合
--------------------
姓名：eric - 身高：166「在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！」
是否适合做接待员：符合
"""
# 从情景从思考适配器
"""
在上面的例子中，高跟鞋起着一个适配的作用，让其形象增高 5~7 厘米完全不在话下，而且效果立竿见影！使得一些女孩原本不符合接待员的真实身高，在鞋子的帮助下也能符合条件。如高跟鞋一样，使原本不匹配某种功能的对象变得匹配这种功能，这在程序中叫做适配器模式。
"""

# 适配器模式
"""
Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

将一个类的接口变成客户端所期望的另一种接口，从而使原本因接口不匹配而无法一起工作的两个类能够在一起工作。
"""

# 适配器的作用
"""
1. 接口转换，将原有的接口（或方法）转换成另一种接口；
2. 用新的接口包装一个已有的类；
3. 匹配一个老的组件到一个新的接口。
"""

# 设计要点—
"""
适配器模式中主要三个角色，在设计适配器模式时要找到并区分这些角色：
1. 目标（Target）： 即你期望的目标接口，要转换成的接口。
2. 源对象（Adaptee）： 即要被转换的角色，要把谁转换成目标角色。
3. 适配器（Adapter）： 适配器模式的核心角色，负责把源对象转换和包装成目标对象。
"""

# 设计思想
"""
适配器模式又叫变压器模式，也叫包装模式（Wrapper）
它的核心思想是将一个对象经过包装或转换后使它符合指定的接口，
使得调用方可以像使用这接口的一般对象一样使用它。
这一思想，在我们生活中可谓是处处可见，
比如变压器插座，能让你像使用国内电器一样使用美标（110V）电器；
还有就是各种转接头，
如 MiniDP 转 HDMI 转接头、HDMI 转 VGA 线转换器、Micro USB 转 Type-C 转接头等。
"""

# 参考链接
# https://gitbook.cn/gitchat/column/5b26040ac81ac568fcf64ea3/topic/5b26052ec81ac568fcf64f20#-2
