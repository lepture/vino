#!/usr/bin/env python

from .query import Query


class Vino(object):
    def __init__(self, db, **kwargs):
        self._db = _connect(db, **kwargs)

    def table(self, name):
        return Query(self._db, name)

    def raw(self, statement):
        return self._db.query(statement)

    def commit(self):
        pass

    @property
    def last_query_time(self):
        return self._db._last_use_time


class _Database(object):
    engine = None
    host = None
    port = None
    user = None
    passwd = None
    dbname = None

    def __init__(self, db):
        # mysql://user:pass@localhost:port/db
        self.engine, host = db.split('://')
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
    global IntegrityError
    global OperationalError

    d = _Database(db)

    if d.engine == 'sqlite':
        from .engines import _sqlite as engine
        IntegrityError = engine.IntegrityError
        OperationalError = engine.OperationalError
        return engine.Connection(d.host)

    elif d.engine == 'mysql':
        from .engines import _mysql as engine
        IntegrityError = engine.IntegrityError
        OperationalError = engine.OperationalError

        max_idle_time = kwargs.pop('max_idle_time', 7 * 3600)
        return engine.Connection(
            d.host, d.dbname, d.user, d.passwd, max_idle_time
        )

    else:
        raise ValueError("Doesn't support %s yet" % d.engine)


IntegrityError = None
OperationalError = None
