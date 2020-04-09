# CombinatorCalculator
A short module designed to check calculations in combinatory algebras.

The usual primitives, `S` and `K` are built in, as are some combinators which are generated by `S` and `K`. Both `S` and `K` are combinators. If `a` and `b` are combinators then so is `a*b` (in this module, *combinators* are elements of the class `Term`). We call `a*b` "`a` applied to `b`". We may see what a combinator does when it is applied by applying it to integers. Each integer `n` is treated as a term which prints as `<n>`. 

```python
>>> from combinators import *
>>> S*0*1*2
<0><2>(<1><2>)
>>> K*0*1
<0>
>>> K*identity*0*1
<1>
>>> B # the B combinator is built in - otherwise known as the bluebird
S(KS)(S(KK)(SKK))
>>> B*0*1*2 # try out the bluebird
<0>(<1><2>)
>>> bluebird(3)*0*1*2*3*4 # there are a whole family of bluebirds, with B = bluebird(1)
<0>(<1><2><3><4>)
>>> projection(1, 0)*0 # projection combinators are built in
<0>
>>> projection(2,0)*0*1
<0>
>>> projection(2,1)*0*1
<1>
>>> projection(5,3)*0*1*2*3*4
<3>
>>> projection(5,3)
K(K(K(S(KK)(SKK))))
```
We can also introduce our own primitives. We may even introduce the mockingbird combinator `M`:
```python
>>> M = Atom("M", lambda x: x*x)
>>> M*0
<0><0>
```
Indeed, we can produce the well-known infinite loop:
```python
>>> M*M
...
RecursionError: maximum recursion depth exceeded
```
We can also construct the mockingbird as `S*identity*identity`:
```python
>>> S*identity*identity*0
<0><0>
```

Sch&ouml;nfinkel's combinator `C` is built in. We can construct the famous `Y` combinator (otherwise known as the "fixed point combinator"):
```python
>>> C
S(S(K(S(KS)K))S)(KK)
>>> C*0*1*2 # try out the C combinator
<0><2><1>
>>> M = S*identity*identity # create the mockingbird
>>> Y = B*M*(C*B*M) # create the Y combinator
```
However, the `Y` combinator gets us in trouble if we try to compute `Y*anything`, but it is an intentional infinite loop:
```python
>>> Y*0
...
RecursionError: maximum recursion depth exceeded while calling a Python object

```
We can deduce a closed term to represent any term, by giving the expression for the term in terms of the variables and using the  `curry` function to "curry out" all of the variables:
```python
>>> x = Atom("x")
>>> y = Atom("y")
>>> z = Atom("z")
>>> curry(x*z*y, x, y, z)
S(S(KS)(S(S(KS)(S(KK)(KS)))(S(S(KS)(S(S(KS)(S(KK)(KS)))(S(S(KS)(S(KK)(KK)))(S(KK)(SKK)))))(S(S(KS)(S(S(KS)(S(KK)(KS)))(S(KK)(KK))))(S(KK)(KK))))))(S(S(KS)(S(KK)(KK)))(S(S(KS)(KK))(KK)))
```
We can even check that this horrifying expression works:
```python
>>> curry(x*z*y, x, y, z)*x*y*z
xzy
```
Clearly `curry` does not produce the friendliest possible representation. This monster is actually just the combinator `C`.

In a couple of stages, we can use currying to derive the `Y` combinator. However, some care must be taken, and it helps to also know how currying works mathematically. The `Y` combinator ought to be such that, for any `f`, `Y*f` is `t*t`, where, for any `x`, `t*x=f*(x*x)`. We can curry `x` out of `t`:
```python
>>> f = Atom("f")
>>> x = Atom("x")
>>> t = curry(f*(x*x), x)
>>> t
S(Kf)(S(SKK)(SKK))
```
However, we cannot simply rush in and calculate `Y = curry(t*t, f)`. This would end up in an infinite loop, as `t*t` also ends up in an infinite loop (intentionally!). But, we can curry `f` out of `t`, and from there we can derive `Y`. As before, we cannot compute `Y*f`:
```python 
>>> u = curry(t, f)
>>> u
S(S(KS)(S(KK)(SKK)))(S(S(KS)(S(S(KS)(KK))(KK)))(S(S(KS)(KK))(KK)))
>>> Y = S*u*u
>>> Y
S(S(S(KS)(S(KK)(SKK)))(S(S(KS)(S(S(KS)(KK))(KK)))(S(S(KS)(KK))(KK))))(S(S(KS)(S(KK)(SKK)))(S(S(KS)(S(S(KS)(KK))(KK)))(S(S(KS)(KK))(KK))))
>>> Y*f
...
RecursionError: maximum recursion depth exceeded
```
