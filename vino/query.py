#!/usr/bin/env python


class Query(object):
    _where_statement = []
    _order_statement = []
    _limit_statement = None
    _offset_statement = None

    def __init__(self, db, table):
        self.db = db
        self.table = table

    def find(self, **kwargs):
        """where statement

        support Django-like queries:

        - ``name__in = []``
        """
        for key in kwargs:
            # TODO: in, like, or
            # bits = key.split('__')
            statement = '%s = "%s"' % (key, kwargs[key])
            self._where_statement.append(statement)

        return self

    def order(self, name):
        direct = 'ASC'
        if name.startswith('-'):
            direct = 'DESC'
            name = name[1:]

        statement = '%s %s' % (name, direct)
        self._order_statement.append(statement)
        return self

    def limit(self, limit):
        self._limit_statement = int(limit)
        return self

    def offset(self, offset):
        self._offset_statement = int(offset)
        return self

    def fetch(self, limit=None, attr=None):
        if limit:
            self._limit_statement = int(limit)

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
        statement.append(self._create_query_statement())
        result = self.db.query(' '.join(statement))

        if limit == 1 and result:
            return result[0]
        return result

    def create(self, **kwargs):
        pass

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    def describe(self):
        pass

    def _create_query_statement(self):
        statement = []
        statement.append('WHERE %s' % 'AND '.join(self._where_statement))
        if self._order_statement:
            order = self._order_statement.pop()
            statement.append('ORDER BY %s' % order)

        if self._offset_statement:
            statement.append('OFFSET %s' % self._offset_statement)

        if self._limit_statement:
            statement.append('LIMIT %s' % self._limit_statement)

        return ' '.join(statement)
