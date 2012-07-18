Vino
=======

VINO Is Not ORM. Yes, it's true, it's not ORM.


Get Started
------------

A quick view with Vino::

    # setup
    # db = Vino('engine://user:passwd@host:port/database')
    db = Vino('sqlite://db.sqlite')

    # query
    db.table('user').find(username='lepture').fetch()

    # create
    db.table('user').create(username='lepture', website='http://lepture.com')
    db.commit()

    # update
    db.table('user').find(username='lepture').update(username='Hsiaoming Yang')
    db.commit()

    # delete
    db.table('user').find(username='lepture').delete()
    db.commit()


Setup
------

We will only support sqlite3 and mysql by now.

SQLite
~~~~~~~

SQLite with relative path::

    db = Vino('sqlite://relative/path/db.sqlite')

SQLite with absolute path::

    db = Vino('sqlite:///root/path/db.sqlite')

**Please note, it's different from SQLAlchemy**.

MySQL
~~~~~~~

MySQL with all information::

    db = Vino('mysql://lepture:123456@localhost:3306/test')

MySQL with less information::

    db = Vino('mysql://lepture@localhost/test')

Default port is 3306.

**Please note, it's utf8 by default**.


Query
------

Find all data::

    db.table('user').find().fetch()

Find all specified data::

    db.table('user').find(username='lepture').fetch()

Find the first data::

    # fetch 1 will not return a list
    db.table('user').find(username='lepture').fetch(1)

Limit on query::

    db.table('user').find(username='lepture').fetch(5, offset=3)

Multiple filters::

    db.table('user').find(username='lepture', age=20).fetch()

Advanced filters::

    # just like Django

    db.table('user').find(age__in=[20, 22]).fetch()
    db.table('user').find(age__gt=20).fetch()
    db.table('user').find(age__lt=20).fetch()
    db.table('user').find(age__gte=20).fetch()
    db.table('user').find(age__lte=20).fetch()

    # more see documentation

More Advanced filters::

    db.table('user').find(age__ne=20).fetch()  # not equal
    db.table('user').find(age__nin=[20, 22]).fetch()  # not in

    # more see documentation

Query order::

    db.table('user').find(age=20).order('-id').fetch()


Create
-------


Update
-------


Delete
---------

Delete all data::

    db.table('user').find().delete()
    db.commit()

Delete specified data::

    db.table('user').find(username='lepture').delete()
    db.commit()


FAQ
-----

1. How do I join tables?

   Vino provides clean and simple API, you should join tables yourself
   with ``db.raw``
