import matchers


class QueryBuilder:
    def __init__(self, query=matchers.All()):
        self.query = query

    def build(self):
        return self.query

    def plays_in(self, team):
        self.query = matchers.And(matchers.PlaysIn(team), self.query)
        return QueryBuilder(self.query)

    def has_at_least(self, value, attr):
        self.query = matchers.And(matchers.HasAtLeast(value, attr), self.query)
        return QueryBuilder(self.query)

    def has_fewer_than(self, value, attr):
        self.query = matchers.And(matchers.HasFewerThan(value, attr), self.query)
        return QueryBuilder(self.query)
