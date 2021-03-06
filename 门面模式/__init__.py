# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-30 23:02
@File    : __init__.py.py
@Describe: 
"""
"""
门面（facade）通常是指定建筑物的表面，尤其是最具有吸引力的那一面，他也可以表示一种容易让人误解某人的真是感受或情况的行为或面貌
当人们从建筑物外面经过时，可以欣赏其外部面貌，却不了解建筑物结构的复杂性，这就是门面模式的使用方式。
门面在隐藏内容系统复杂性的同时，为客户端提供一个接口，以便他们可以非常轻松地访问系统。
下面，我们以店主为例进行介绍，现在，假设你要到某个商店去买东西，但是你对这个商店的布局并不清楚，
通常情况下，你会找店主，因为店主对整个商店都很清楚，只要你告诉他你要买什么，店主就会把商品拿给你，这不是很容易吗。
顾客不必了解店面的情况，可以通过一个简单的接口来完成购物，这里的接口就是店主
"""
# 门面模式完成了以下事项：
"""
1. 他为子系统中的一组接口提供一个统一的接口，并定义一个高级接口来帮助客户端通过更简单的方式使用子系统。
2. 门面所解决是，如果用单个接口对来表示复杂的子系统，他并不是封装子系统，而是对底层子系统进行组合
3. 它促进了实现与多个客户端的解耦
"""

# 门面模式有3个主要的参与者：
"""
门面：门面的主要责任是，将一组复杂系统封装起来，从而为外部世界提供一个舒适的外观。
系统：这代表一组不同子系统，是整个系统混杂在一起，难以观察或使用
客户端：客户端与门面进行交互，这样就可以轻松的与子系统进行通信并完成工作了，不必担心系统的复杂性
"""

# 现在我们将会从数据结构的角度进一步介绍这三个参与者：
# 门面 #
# 以下几点可以帮助我们更好的理解门面
"""
1. 他是一个接口，他知道某个请求可以交由那个子系统进行处理
2. 他使用组合将客户端的请求委派给响应的子系统对象
例如：
如果客户端正在了解哪些工作已经完成，则不需要到各个子系统中去，相反，他只需要联系完成工作的接口（门面）就可以了。
"""

# 系统 #
# 在门面的世界里，系统就是执行以下操作的实体
"""
1. 他实现子系统的功能，同时，系统有一个类表示，理想情况下，系统应该由一组负责不同任务的类来表示
2. 系统处理门面对象分配的工作，但并不知道门面，而且不可引用他
例如：
当客户端向门面请求某项服务时，门面会根据服务的类型来选择提供该服务的响应子系统
"""

# 客户端 #
# 以下是对客户端的描述
"""
1. 客户端是实例化门面的类
2. 为了让子系统完成响应的工作，客户端需要向门面提出请求
"""

# 在现实世界中实现门面模式
# 为了演示门面模式的应用，让我们举个生活中的例子。
"""
    假设你要在家中举办一场婚礼，并且由你张罗这一切，这真是一个艰巨的任务，你必须预定一家酒店或场地，
与餐饮人员交代酒店，布置场景，并安排背景音乐。
    在不久以前，你已经自己搞定了一切，例如找相关人员谈话，与他们进行协调，敲定价格等，那么现在你就很轻松了，此外你还可以找会务经理，
让他为你处理这些事情，会务经理负责和各个服务提供商进行交涉，并为你争取最优的价格。
"""
# 下面我们从门面模式的角度来看待这个问题
"""
 
    （你）需要再婚礼前及时完成所有的准备工作，每一项安排都应该是顶级的,这样客人才会喜欢这些庆祝活动
门面：
    （会务经理）负责与所有相关人员进行交涉，这些人员负责处理食物，花卉，装饰等。
子系统：
    （我们）代表提供餐饮，酒店管理和花卉装饰等服务的系统，
"""

# TODO：page 57

