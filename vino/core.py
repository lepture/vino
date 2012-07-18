#!/usr/bin/env python


class Vino(object):
    last_query = None
    last_query_time = None

    def __init__(self, db):
        self._database = _connect(db)

    def table(self, name):
        pass

    def raw(self, statement):
        pass

    def commit(self):
        pass


def _connect(db):
    pass
