#!/usr/bin/env python

import time
from .query import Query


class Vino(object):
    last_query_time = time.time()

    def __init__(self, db, **kwargs):
        self._db = _connect(db, **kwargs)

    def table(self, name):
        self.last_query_time = time.time()
        return Query(self._db, name)

    def raw(self, statement):
        self.last_query_time = time.time()
        pass

    def commit(self):
        self.last_query_time = time.time()
        pass


class _Database(object):
    engine = None
    host = None
    port = None
    user = None
    passwd = None
    dbname = None

    def __init__(self, db):
        # mysql://user:pass@localhost:port/db
        self.engine, host = db.splite('://')
        if '@' not in host:
            self.host = host
            return

        self.user, host = host.split('@')
        if ':' in self.user:
            self.user, self.passwd = self.user.split(':')

        self.host, self.dbname = host.split('/')
        if ':' in self.host:
            self.host, self.port = self.host.split(':')


def _connect(db, **kwargs):
    d = _Database(db)
    if d.engine == 'sqlite':
        from .engines._sqlite import Connection
        return Connection(d.host)
    elif d.engine == 'mysqlite':
        from .engines._mysql import Connection
        max_idle_time = kwargs.pop('max_idle_time', 7 * 3600)
        return Connection(d.host, d.dbname, d.user, d.passwd, max_idle_time)
    else:
        raise ValueError("Doesn't support %s yet" % d.engine)
