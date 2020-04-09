class Combinator:
    def __init__(self, left, relation=None):
        self.left = left
        self.right = None
        self.relation = relation

    def __len__(self):
        if self.right:
            return len(self.left) + len(self.right)
        else:
            return len(self.left)

    def __bool__(self):
        return True

    def __str__(self):
        if self.right:
            if len(self.right) == 1:
                return str(self.left) + str(self.right)
            else:
                return str(self.left) + "(" + str(self.right) + ")"
        else:
            return str(self.left)

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        if isinstance(other, int):
            return self * Atom("<{}>".format(other))
        else:
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


class Atom(Combinator):
    def __init__(self, left, relation=None):
        super().__init__(left, relation)

    def __len__(self):
        return 1
