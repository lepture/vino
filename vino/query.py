#!/usr/bin/env python


class Query(object):
    def __init__(self, table):
        self.table = table

    def find(self, **kwargs):
        for key in kwargs:
            bits = key.split('__')

        pass

    def order(self, order):
        reverse = False
        if order.startswith('-'):
            reverse = True
            order = order[1:]

        pass
