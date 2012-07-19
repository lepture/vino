#!/usr/bin/env python


class Query(object):
    _where_statement = []
    _order_statement = []
    _end_of_statement = False

    def __init__(self, db, table):
        self.db = db
        self.table = table

    def find(self, **kwargs):
        """where statement

        support Django-like queries:

        - ``name__in = []``
        """
        if self._end_of_statement:
            return self

        for key in kwargs:
            # TODO: in, like, or
            # bits = key.split('__')
            statement = '%s = "%s"' % (key, kwargs[key])
            self._where_statement.append(statement)

        return self

    def order(self, name):
        if self._end_of_statement:
            return self

        direct = 'ASC'
        if name.startswith('-'):
            direct = 'DESC'
            name = name[1:]

        statement = '%s %s' % (name, direct)
        self._order_statement.append(statement)
        return self

    def fetch(self, limit=None, offset=None, attr=None):
        self._end_of_statement = True
        statement = []
        if attr:
            if isinstance(attr, basestring):
                select = attr
            else:
                select = ', '.join(attr)
        else:
            select = '*'
        statement.append('SELECT %s' % select)
        statement.append('FROM %s' % self.table)
        statement.append('WHERE %s' % 'AND '.join(self._where_statement))
        if self._order_statement:
            order = self._order_statement.pop()
            statement.append('ORDER BY %s' % order)

        if offset:
            statement.append('OFFSET %s' % limit)

        if limit:
            statement.append('LIMIT %s' % limit)

        return self.db.query(' '.join(statement))

    def create(self, **kwargs):
        self._end_of_statement = True
        pass

    def update(self, **kwargs):
        self._end_of_statement = True
        pass

    def delete(self, **kwargs):
        self._end_of_statement = True
        pass

    def describe(self):
        self._end_of_statement = True
        pass
