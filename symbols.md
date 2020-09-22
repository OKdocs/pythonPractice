# symbols

## keywords

word | purpose
--- | ---
and | regular logical 'and' operator '&&' in go
or | regular logical 'or' operator '||' in go
not | logical 'not' operator like '!=' in go
del | delete / remove object or variable from memory
from | used for imports from file from relative path ```from .moduleY import functionY as aliasX```
import | import package 
as | import as alias ```import pandas as pd```
yield | returns generator object that behaves like iterator
yield from | with yield statement build generator using iterator ``` yield from <iterator>```
if | starts the 'if' statement ```if condition == True:```
elif | adds a second conditional statement ```elif == True```
else | adds a unconditional conditional statement
while | starts a while loop ```while condition == True:```
for | starts loop over iterator ```for elementX in interatorY:```
in | used to state iterator in for-loop and to check if element is found in array
continue | ends current and continues with next iteration in for-loop, same as in go
break | ends for-loop, same as in go
def | define function, 'func' in go
lambda | define ananonymous function, ```lambda input:output```
return | ends function and returns result to caller, like in go

with | 
assert | 
pass | 
except |
class |
exec | 
raise | 
finally | 
is |
try |


## generators
are smaller than arrays or similar things but can also function as iterators, decrease iterator size
```py
def stringIterator(str):
  yield from str
```
  will return iterator (works like array of chars, but can be much smaller, particularly if it is math)
  ## loops
  ### for in loop
  python style loop requires an iterator, loop loops over all elements of the iterator
  ```py 
  for s in stringIterator(str):
    print(s)
  ```
 C-style loops (init;while condition;post) aren't idiomatic python, use generators with yield or range keyword to create iterators on the fly
 ```py
 for i in range(0,10):
  print(i)
 ```
 would be equivalent to
 ```go
 for i:=0; i <10; i++{
 fmt.Println(i)
 }
 ```
  ### while loop
  
  
  ## condition
  
