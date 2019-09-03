# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-08-25 18:34
@File    : 代理模式.py
@Describe: 
"""
"""
在下面这个例子中,其中Actor是代理, 对象Agent用于查看Actor是否处于忙碌的状态, 如果Actor正忙, 则调用Actor().occupied(), 如果Actor不忙, 则返回Actor().available()
"""


class Actor(object):

    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.is_busy = False
        print(type(self).__name__, "is free for the movie")

    def get_status(self):
        return self.is_busy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()

"""
代理模式住要完成一下的工作:
1. 他为其他对象提供一个代理, 从而实现了对原始对象的访问控制
2. 他可以作为一个层或接口,以支持分布式访问
3. 他通过增加代理, 保护真正的组件不受意外的影响
"""