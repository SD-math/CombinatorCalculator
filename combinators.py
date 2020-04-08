class Term:
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
                result = Term(self)
                result.right = other
                return result
            else:
                val = self.relation(other)
                if isinstance(val, Term):
                    return val
                else:
                    result = Term(self, val)
                    result.right = other
                    return result


class Atom(Term):
    def __init__(self, left, relation=None):
        super().__init__(left, relation)

    def __len__(self):
        return 1


S = Atom("S", lambda x: lambda y: lambda z: (x * z) * (y * z))  # the melting function
K = Atom("K", lambda x: lambda y: x)  # the kestrel
C = (S * (S * (K * (S * (K * S) * K)) * S) * (K * K))
identity = S * K * K  # the identity


def bluebird(n):
    if n:
        return S * (K * S) * (S * (K * K) * (bluebird(n - 1)))
    else:
        return identity


def melting_function(n):
    if n:
        return S * melting_function(n - 1)
    else:
        return identity


def projection(n, i):
    if n > 1:
        if i:
            return K * projection(n - 1, i - 1)
        else:
            return bluebird(n - 1) * K * projection(n - 1, i)
    else:
        return identity


__S = Atom("S")
__K = Atom("K")


def atoms_in(term):
    if term.right:
        return atoms_in(term.left) | atoms_in(term.right)
    else:
        return {term.left}


def curry(term, *args):
    if len(args) > 1:
        return curry(curry(term, args[-1]), *args[:-1])
    else:
        arg = args[0]
        if term.right:
            if arg in atoms_in(term):
                return K * term
            else:
                return S * (curry(term.left, arg)) * (curry(term.right, arg))
        else:
            if term is arg:
                return identity
            else:
                return K * term
