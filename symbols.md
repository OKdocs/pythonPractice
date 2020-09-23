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
else | adds a unconditional conditional statement, in error handling block executed if no error was raised
while | starts a while loop ```while condition == True:```
for | starts loop over iterator ```for elementX in interatorY:```
in | used to state iterator in for-loop and to check if element is found in array
continue | ends current and continues with next iteration in for-loop, same as in go
break | ends for-loop, same as in go
def | define function, 'func' in go
lambda | define ananonymous function, ```lambda input:output```
return | ends function and returns result to caller, like in go
with | with block ensures clean-up code to be run, use for example to open files
assert | if condition is false, return assertionError ```assert condition, assertionError``` run python with ```-o``` (optimized) to disable all assertions
pass | empty method or function, placeholder until written
try | starts error handling block, contains block of code that could cause error
except | if error is raised, except statement is executed, can be specified for particlar error
finally | executed after error handling block, regardless of error
raise | raise an error / exception, must state valid error type

class |
exec | 
is |


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
  
  ## error handling
  errors can be handled in with ```try``` ```except``` ```else``` and ```finally``` keywords
  ```py
  try:
    condition
  except:
    print("Error was raised")
  else: 
    print("Everything worked")
  finally:
    print("Execute me no matter what")
 ```
 the ```try``` is stating the condition, if error is raised, ```except``` is executed, no error leads to execution of ```else``` block, ```finally``` will be executed under all circumstances
 
 ```py
 try:
  condition
 except errorType1:
  # handle errorType1
 except errorType2:
  # handle errorType2
 except errorType3:
  # handle errorType3 
 except:
  # handle all other errorTypes
 ```
 exceptions can selectively catch errors, or all errors depended on syntax
  
