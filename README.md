# CombinatorCalculator
A short module designed to help check calculations in combinatory algebras

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
>>> M = Atom("M", lambda x: x * x)
>>> M*0
<0><0>
```
Indeed, we can produce the well-known infinite loop:
```python
>>> M*M
...
RecursionError: maximum recursion depth exceeded
...
```
We can also construct the mockingbird as `S*identity*identity`:
```python
S*identity*identity*0
<0><0>
```
