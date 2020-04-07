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

```
