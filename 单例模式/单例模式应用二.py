# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-29 21:49
@File    : 单例模式应用二.py
@Describe: 
"""

"""
让我们考虑另外一种情况，即为基础设施提供运行状态监控服务，我们创建了HealthCheck类，
他作为单例模式实现，我们还要维护一个被监控的服务器列表。当一个服务器从这个列表中删除时，
监控软件应该察觉到这一情况，并且从被监控的服务器列表中将其删除。

在下面代码中，hc1和hc2对象与单例中的类一样

我们可以使用addServer()方法将服务器添加到基础设施中,以进行运行状态的检查，
首先，通过迭代对这些服务器的运行状况进行检查，之后，changeServer()方法将会删除最后一个服务器，
并向计划进行运行状况检查的基础设施中添加一个新的服务器，因此，当运行状况检查进行第二次迭代，
他会使用修改后的服务器列表。
"""


class HealthCheck(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        self.server = []
        # 单例模式共享资源

    def add_server(self):
        self.server.append("server 1")
        self.server.append("server 2")
        self.server.append("server 3")
        self.server.append("server 4")

    def change_server(self):
        self.server.pop()
        self.server.append("server 5")


if __name__ == '__main__':
    hc1 = HealthCheck()
    hc2 = HealthCheck()
    hc1.add_server()
    print("schedule health check for servers...")

    for i in range(4):
        print("checking", hc1.server[i])

    hc2.change_server()
    for i in range(4):
        print("checking ", hc2.server[i])
