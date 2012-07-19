#!/usr/bin/env python


class Query(object):
    __finds = []
    __orders = []
    __end_of_statement = False

    def __init__(self, db, table):
        self.db = db
        self.table = table

    def find(self, **kwargs):
        if self.__end_of_statement:
            return self

        for key in kwargs:
            bits = key.split('__')

        return self

    def order(self, order):
        if self.__end_of_statement:
            return self

        reverse = False
        if order.startswith('-'):
            reverse = True
            order = order[1:]

        return self

    def fetch(self, limit=None, offset=None, attr=None):
        self.__end_of_statement = True
        pass

    def create(self, **kwargs):
        self.__end_of_statement = True
        pass

    def update(self, **kwargs):
        self.__end_of_statement = True
        pass

    def delete(self, **kwargs):
        self.__end_of_statement = True
        pass

    def describe(self):
        self.__end_of_statement = True
        pass
