# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-08-25 16:41
@File    : 门面模式.py
@Describe: 
"""


class EventManager(object):

    def __init__(self):
        print("Event Manger")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


"""
现在我们已经搞定了门面和客户端,下面开始深入了解子系统
1. Hotelier类用于预定酒店,他有一个方法, 用于检查当前是否有免费的酒店
2. Florist类负责花卉装饰,这个类提供了set_flower_requirements方法,用于指定要使用那些中类的花卉来装饰婚礼
3. Caterer类用于跟备办宴席这打交道,并负责安排餐饮,Caterer提供一个公开的方法set_cuisine方法,用来指定婚宴的菜肴类型
4. Musician类用来安排婚礼的音乐,他使用set_music_type来了解会务的音乐要求
接下来让我们先来考察Hotelier对象,其次是Florist对象及其方法
"""


class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage")

    def __is_available(self):
        print("is the hotel free for the event one give day?")
        return None

    def book_hotel(self):
        if self.__is_available():
            print("Register the booking")


class Florist(object):
    def __init__(self):
        print("flower decorations for the event?")

    def set_flower_requirements(self):
        print("Carnations roses and lilies would be used for decorations\n\n")


class Caterer(object):
    def __init__(self):
        print("Food arrangements for the event")

    def set_cuisine(self):
        print("chinese & continental cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("Musical arrangements for events")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


"""
但是你很聪明,所以将这些事情都委托给会务经理,不是吗? 让我们来看看You类,在本示例中,创建一个EventManger实例,这样会务经理会通过与相关人员进行交涉来筹备婚礼,而你可以找个地方喝茶了
"""


class You(object):
    def __init__(self):
        print("You: Whoa! Marriage Arrangements???!!!")

    def ask_event_manager(self):
        print("You: let contact the event manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You: thanks to events manager, all preparations done! Phew")


you = You()
you.ask_event_manager()

"""
我们可以通过以下方式将门面模式与真实世界场景相关联
1. EventManager类是简化接口的门面
2. EventManger通过组合创建子系统的对象, 如Hotelier,Caterer等等
"""

# 最少只是原则
"""
正如本章的开始部分介绍的那些, 门面为我们提供了一个统一的子系统,他使得子系统更加易于使用,
他将客户端与子系统解耦,门面模式本周的设计原理就是最少知识原则.
最少知识原则知道我们减少对象之间的交互,就像跟你亲近的只有某几个朋友那样.实际上,它意味着:
1. 在设计系统时,对于创建的每一个对象,都应该考察与之交互的类型的数量,以及交互的方式.
2. 遵循这个原则,就能避免创建许多彼此紧密耦合的类的情况
3. 如果类之间存在大量的依赖关系, 那么系统就会变得难以维护,如果对子系统中的任何一部分进行修改,都可能导致系统的其他地方被无意的改变,这意味这系统会退化,这种情况应该坚决避免的.
"""
