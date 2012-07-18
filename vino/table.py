#!/usr/bin/env python

from .query import Query


class Table(object):
    _query = None

    def __init__(self, name):
        self.name = name

    @property
    def query(self):
        if self._query:
            return self._query
        self._query = Query(self.name)
        return self._query

    def find(self, **kwargs):
        pass

    def update(self, **kwargs):
        pass

    def create(self, **kwargs):
        pass

    def fetch(self, limit=None, offset=None):
        pass

    def order(self, order):
        pass
