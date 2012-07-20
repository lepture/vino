from vino.query import Query


class TestQuery(object):
    def test_create_query_statement(self):
        q = Query(None, 'user')
        q.find(a='a')
        q.find(a='abc')  # this should be ignored
        assert q._create_query_statement() == 'WHERE a = "a"'

    def test_create_query_statement2(self):
        q = Query(None, 'user')
        q.find(b='b')
        q.order('-id')
        assert q._create_query_statement() == 'WHERE b = "b" ORDER BY id DESC'
