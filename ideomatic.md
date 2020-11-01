
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
  
  while loops iterate over a code block while the test condition is true
  ```py
  while condition_true:
    do stuff
  ```
  everything is considered ```True``` execpt for ```False```, ```None``` and ```0``` 
### iteration control
  ```break``` and ```continue``` statements exists like in other languages
### iterators
```range```

```reversed```

```enumerate```

#### generators
are smaller than arrays or similar things but can also function as iterators, decrease iterator size
```py
def stringIterator(str):
  yield from str
```
  will return iterator (works like array of chars, but can be much smaller, particularly if it is math)
## condition
  
  three statements handle conditions in python:
  + if
  + elif
  + else

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
  
 ## defining functions
 ```def```
 
 ### arguments
 
 ```*arg```
 variable amount of arguments, similar to passing an list
 ```**kvargs```
 variable amount of key:value arguments, similar to passing a dictionary
 
