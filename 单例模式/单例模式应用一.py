# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei

@Time    : 2019-07-28 21:53
@File    : 单例模式应用一.py
@Describe: 
"""
import sqlite3


class MateSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MateSingleton, cls).__call__()
        return cls.__instances[cls]


class DataBase(metaclass=MateSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("ddb.sqlite3")
            self.cursorobj = self.connection.cursor()

        return self.cursorobj


if __name__ == '__main__':
    db1 = DataBase()
    db2 = DataBase()
    print(db1, db2)
