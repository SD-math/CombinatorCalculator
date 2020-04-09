from combinators import *

S = Atom("S", lambda x: lambda y: lambda z: (x * z) * (y * z))  # the melting function
K = Atom("K", lambda x: lambda y: x)  # the kestrel
C = (S * (S * (K * (S * (K * S) * K)) * S) * (K * K))
identity = S * K * K  # the identity


def bluebird(n):
    if n:
        return S * (K * S) * (S * (K * K) * (bluebird(n - 1)))
    else:
        return identity


B = bluebird(1)


def projection(n, i):
    """
    :param n: A non-negative integer
    :param i: A non-negative integer i<n
    :return: A combinator which expresses projection onto the i-th component, for an n-tuple
    """
    if n > 1:
        if i:
            return K * projection(n - 1, i - 1)
        else:
            return bluebird(n - 1) * K * projection(n - 1, i)
    else:
        return identity


def atoms_in(term):
    """
    :param term: A combinator
    :return: A set consisting of all atoms which occur in the input
    """
    if term.right:
        return atoms_in(term.left) | atoms_in(term.right)
    else:
        return {term}


def curry(term, *args):
    """
    Gives a way of translating from a primitive's reduction rule to a closed term in the SK basis.
    This could be viewed as abstraction.
    :param term: A term.
    :param args: Which atoms you wish to curry out of the term, in the order you wish them to appear.
    :return: In the following examples, x, y, z are atoms, e.g. x = identity*0, y = identity*1, z = identity*2.
    Alternatively x = Atom("x"), y = Atom("y"), z = Atom("z").
    E.g. curry(x*z*y*z*x*x, x) will give a term t in y, z such that t*x = x*z*y*z*x*x.
    E.g. curry(y*x*z, x, y) will give a term t in z such that t*x*y = y*x*z.
    E.g. curry(x*y*x*z, x, y, z) will give a closed term t such that t*x*y*z = x*y*x*z.
    """
    if len(args) > 1:
        return curry(curry(term, args[-1]), *args[:-1])
    else:
        arg = args[0]
        if arg in atoms_in(term):
            if term.right:
                return S * curry(term.left, arg) * curry(term.right, arg)
            else:
                return identity
        else:
            return K * term
