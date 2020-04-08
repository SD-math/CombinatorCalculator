# CombinatorCalculator
A short module designed to help check calculations in combinatory algebras.

The usual primitives, `S` and `K` are built in, as are some combinators which are generated by `S` and `K`.

```python
>>> from combinators import *
>>> S*0*1*2
<0><2>(<1><2>)
>>> K*0*1
<0>
>>> K*identity*0*1
<1>
>>> B = bluebird(1)
>>> B
S(KS)(S(KK)(SKK))
>>> B*0*1*2
<0>(<1><2>)
>>> bluebird(3)*0*1*2*3*4
<0>(<1><2><3><4>)
>>> projection(1, 0)*0
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
We can also introduce our own primitives. We may even introduce the mockingbird combinator `M':
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

Sch&ouml;nfinkel's combinator `C` is hard-coded. We can construct the famous `Y` combinator (otherwise known as the "fixed point combinator"):
```python
>>> C
S(S(K(S(KS)K))S)(KK)
>>> C*0*1*2 # try out the C combinator
<0><2><1>
>>> M = S*identity*identity # create the mockingbird
>>> B = bluebird(1)
>>> Y = B*M*(C*B*M) # create the Y combinator
```
However, the `Y` combinator gets us in trouble if we try to compute `Y*anything`, but it is an intentional infinite loop:
```python
>>> Y*0
...
RecursionError: maximum recursion depth exceeded while calling a Python object

```
We call an Atom without a rule a *variable*. We can deduce a closed term to represent any term, by giving the expression for the term in terms of the variables and using the  `curry` function to "curry out" all of the variables:
```python
>>> x = Atom("x")
>>> y = Atom("y")
>>> z = Atom("z")
>>> curry(x*z*y,x, y, z)
S(S(KS)(S(S(KS)(S(KK)(KS)))(S(S(KS)(S(S(KS)(S(KK)(KS)))(S(S(KS)(S(KK)(KK)))(S(KK)(SKK)))))(S(S(KS)(S(S(KS)(S(KK)(KS)))(S(KK)(KK))))(S(KK)(KK))))))(S(S(KS)(S(KK)(KK)))(S(S(KS)(KK))(KK)))
```
