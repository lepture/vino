#!/usr/bin/env python


def create(table, schema):
    """create table via schema
    {
        "columns": {
            "id": {
                "type": "integer",
                "null": False,
            },
            "username": {
                "type": "varchar",
                "length": 50,
                "null": False,
                "unique": True,
            },
            "email": {
                "type": "varchar",
                "length": 200,
                "null": False,
                "unique": True,
            },
            "created": {
                "type": "datetime"
            }
        },
        "index": [
            "username",
        ],
        "primary": "id",
    }
    """

    statement = ["CREATE TABLE %s (" % table]
    columns = schema['columns']
    for key in columns:
        column = columns[key]
        column_type = column['type']
        if column_type == 'varchar':
            column_type == '%s(%s)' % (column_type, column['length'])
        line = '%s %s' % (key, column_type)

        #TODO unique
        if 'null' in column and column['null'] is False:
            line += ' NOT NULL,'
        else:
            line += ','

        statement.append(line)

    statement.append('PRIMARY KEY (%s)' % columns['primary'])
    statement.append(');')
    return '\n'.join(statement)
