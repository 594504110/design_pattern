# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-04-27 16:00
@Software: PyCharm
@File    : __init__.py.py
"""
"""
单例模式
实现单例模式的一个简单的方法是:
使构造函数私有化,并创建一个静态方法来完成对象的初始化,这样,对象将在第一次调用是创建,此后这个类都返回同一个对象
"""

# 单例模式的缺点
"""
虽然单例模式在许多情况下效果很好，但这种模式仍然存在缺陷，由于单例模式具有全局访问权限，因此可能会出现以下问题：
1. 全局变量可能在某处已经被误改，但是开发人员仍然认为他们没有发生变化，而该变量还在应用程序的其他位置被使用。
2. 可能会对同一个对象创建多个索引，由于单例模式之创建一个对象，因此这种情况下会对同一个对象创建多个引用。
3. 所有依赖环境变量的类都会由于一个类的改变而紧密耦合为全局数据，从而可能在无意中影响另一个类
"""

# 使用单例模式的小技巧
"""
1. 在许多实际的应用程序中，我们只需要创建一个对象，如线程池，缓存，对话框，注册表设置等，
如果我们为每一个应用程序创建对多个示例，则会导致资源的过度使用，单例模式在这种情况下表现的很好。

2. 单例模式是一种经过时间考验的成熟方法，能够在不带看来太多缺陷的情况下提供全局访问点

3. 当然，该模式也有几个缺点，当使用全局变量或类的实例化非常耗费资源但最终却没有用到他们的情况下，单例的影响可忽略不计
"""
