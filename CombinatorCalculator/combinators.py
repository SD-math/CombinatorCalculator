class Combinator:
    def __init__(self, left, relation=None):
        self.left = left
        self.right = None
        self.relation = relation

    def __bool__(self):
        return True

    def __str__(self):
        if self.right:
            if isinstance(self.right, Atom):
                return str(self.left) + str(self.right)
            else:
                return str(self.left) + "(" + str(self.right) + ")"
        else:
            return str(self.left)

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        if isinstance(other, Combinator):
            if self.relation is None:
                result = Combinator(self)
                result.right = other
                return result
            else:
                val = self.relation(other)
                if isinstance(val, Combinator):
                    return val
                else:
                    result = Combinator(self, val)
                    result.right = other
                    return result
        else:
            return self * Atom(other)


class Atom(Combinator):
    def __init__(self, left, relation=None):
        super().__init__(left, relation)
