
# Case 1: Goi func tu 1 class nam trong file py khac

```python
# create file mymodule.py
import random as rd

class myFunc:
    def random_number_generator(input):
        l_array=[]
        for i in range(0, input):
            e = rd.randint(0, i)
            l_array.append(e)

        return l_array

# myrun.py
from mymodule import *

abc = myFunc()
result = abc.random_number_generator(19)
print(result)
```

*2 loi se gap tuong tu nhau*

`ERROR: AttributeError: 'myFunc' object has no attribute`
---------------------------------------------------------------------------
NameError Traceback (most recent call last)
<ipython-input-2-a98f9a0223bd> in <module>
      1 from lab8 import *
----> 2 rf = myFunc()
      3 result = rf.random_number_generator(19)

NameError: name 'myFunc' is not defined

`ERROR: AttributeError: 'myFunc' object has no attribute 'random_number_generator'`
---------------------------------------------------------------------------
AttributeError Traceback (most recent call last)
<ipython-input-3-39dfcd21ae94> in <module>
      3 abc = myFunc()
      4 
----> 5 result = abc.random_number_generator(10)
      6 print(result)

AttributeError: 'myFunc' object has no attribute 'random_number_generator'

`Solution: Restart session if using notebook`


*Sau khi restart session se gap loi khac*
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-1-39dfcd21ae94> in <module>
      3 abc = myFunc()
      4 
----> 5 result = abc.random_number_generator(10)
      6 print(result)

TypeError: random_number_generator() takes 1 positional argument but 2 were given

`Solution: In Python you should add self argument as the first argument to all defined methods in classes:`

```python
import random as rd

class myFunc:
    def random_number_generator(self, input):
        self.l_array=[]
        for i in range(0, input):
            e = rd.randint(0, i)
            self.l_array.append(e)

        return self.l_array
```

Then you can use your method according to your intuition:
```python
from mymodule import *

abc = myFunc()

result = abc.random_number_generator(19)
print(result)
```
[0, 0, 0, 1, 0, 3, 3, 1, 8, 0, 3, 0, 2, 2, 0, 10, 15, 2, 8]

This should solve your problem :)

Refer: [typeerror-method-takes-1-positional-argument-but-2-were-given](https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given)


## TypeError: Cannot interpret '<attribute 'dtype' of 'numpy.generic' objects>' as a data type
```py
#Reproducing code example:
import numpy as np
<< your code here >>
import numpy as np
import pandas as pd
df=pd.read_csv('link')
df.info() and df.describe() gives error as "TypeError: Cannot interpret '<attribute 'dtype' of 'numpy.generic' objects>' as a data type" and also plotting(df.plot()) gives same error.
```
`Accepted Answer`
```
There is a unfortuate incompatibility with old pandas and 1.20. Updating pandas to a newer version should fix it, see also pandas-dev/pandas#39520 (comment)

Updating to pandas>=1.0.5 should solve it. Supposedly also pandas==0.25.3 works. If you are stuck with pandas 0.24.x you may not be able to usse numpy 1.20.x though, unfortunaly. In that case, use numpy<1.20
```
Refer: [typeerror-cannot-interpret-attribute-dtype-of-numpy-generic-objects-as-a-data-type](https://lifesaver.codes/answer/typeerror-cannot-interpret-attribute-dtype-of-numpy-generic-objects-as-a-data-type-18355)

