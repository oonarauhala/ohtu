import matchers


class QueryBuilder:
    def __init__(self, query=matchers.All()):
        self.query = query

    def build(self):
        return self.query

    def plays_in(self, team):
        return QueryBuilder(matchers.And(matchers.PlaysIn(team), self.query))

    def has_at_least(self, value, attr):
        return QueryBuilder(matchers.And(matchers.HasAtLeast(value, attr), self.query))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(
            matchers.And(matchers.HasFewerThan(value, attr), self.query)
        )

    def one_of(self, first, second):
        return QueryBuilder(matchers.Or(first, second))
