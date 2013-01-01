#!/usr/bin/env python
# coding: utf-8

import logging


class Query(object):
    def __init__(self, db, table):
        self.db = db
        self.table = table

        self._where_statement = []
        self._order_statement = []
        self._limit_statement = None
        self._offset_statement = None
        self._find_kwargs = []

    def find(self, **kwargs):
        """where statement

        support Django-like queries:

        - ``name__in = []``
        """

        def parse(opt, value):
            if opt == 'like' or opt == 'contains':
                return 'LIKE', ''.join(['%', value, '%'])
            if opt == 'startswith':
                return 'LIKE', ''.join([value, '%'])
            if opt == 'endswith':
                return 'LIKE', ''.join(['%', value])
            if opt == 'in' and isinstance(value, (list, tuple)):
                if len(value) == 0:
                    return None
                if len(value) == 1:
                    return '=', value[0]
                #TODO unicode
                return 'IN', str(value)
            return opt.upper(), value

        for key in kwargs:
            bits = key.split('__')
            name = bits[0]
            if len(bits) > 1:
                opt = bits[1]
            else:
                opt = '='

            opt, value = parse(opt, kwargs[key])

            if name in self._find_kwargs:
                logging.warn('%s already in clause, ignore' % name)
            elif value:
                statement = '%s %s "%s"' % (name, opt, value)
                self._where_statement.append(statement)
                self._find_kwargs.append(name)

        return self

    def where(self, **kwargs):
        # this is an alias of find
        return self.find(**kwargs)

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

    def fetch(self, attr=None):
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

        if self._limit_statement == 1 and result:
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

    def count(self):
        return self.db.query('SELECT count(*) FROM %s' % self.table)

    def _create_query_statement(self):
        statement = []
        statement.append('WHERE %s' % ' AND '.join(self._where_statement))
        if self._order_statement:
            order = self._order_statement.pop()
            statement.append('ORDER BY %s' % order)

        if self._offset_statement:
            statement.append('OFFSET %s' % self._offset_statement)

        if self._limit_statement:
            statement.append('LIMIT %s' % self._limit_statement)

        return ' '.join(statement)
