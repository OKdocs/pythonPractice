# symbols

## keywords

word | purpose
--- | ---
and | regular logical 'and' operator '&&' in go
or | regular logical 'or' operator '||' in go
not | logical 'not' operator like '!=' in go
is | test is two objects are the same, different from '==' that test if they are equal
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
class | defines a class
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
exec | executes python code, sounds weird, but can be used for example to run scripts

## data types

type | description
--- | ---
True | boolean true
False | boolean false
None | null variable (null pointer)
strings | arrays of bytes representing unicode
numbers | integers have no dot ```x=5``` is integer
floats | floats have dot ```x=5.0``` is float
complex | complex numbers created with function call ```x=complex(5,0)```  

collection | ordering and duplicates | changeability (mutable) | key:value
--- | --- | ---
lists | ordered and duplicates | changeable | key
tuples | ordered and duplicates | unchangeable | key
set | unordered no duplicates | changeable | key
dictionary | unordered no duplicates | changeable | key:value


## string escape sequences

escape sequence | effect
--- | ---
\\ | \
\' | '
\" | "
\a | bell (makes sound)
\b | backspace (delete last character)
\f | formfeed: start new line and continue writing where last line ended
\n | new line
\r | restart writing at the start of current line, overwrites old text
\t | tab
\v | vertigal tab: looks to me like formfeed

## string formats
more info https://docs.python.org/3.4/library/string.html

symbol | format
--- | ---
%d | decimal integer (preferred)
%i | decimal integer (use d instead)
%o | octol integer (base 8)
%u | decimal integer, not listed in docs (mysterious)
%x | hex integer (base 16, lowercase letters)
%X | hex integer (base 16, uppercase letters)
%e | scientific exponent notation (lowercase 'e')
%E | scientific exponent notation (uppercase 'E')
%f | fixed point, can include %.2f to limit numbers after '.'
%F | fixed point, but "NAN" and "INF" in uppercase
%g | general format: depended on value calls fixed point(%f) or scientific format(%e) 
%G | general format, but "NAN","INF" and "E" instead of lowercase equivalents
%c | character, converts integers to unicode if necessary
%r | prints what ever it reads as string, even '\r' and other formating comands
%s | string
%% | percentage: multiplies by 100 calls %f and adds "%" at the end 

## operators

symbol | effect
--- | ---
+ | addition
- | subtraction
* | multiplication
** | exponentiation (to the power of)
/ | division
// | division and floor result (stays integer)
% | remainder
< | lesser/smaller than
> | bigger than
<= | lesser/smaller or equal 
>= | bigger or equal
== | equal
!= | not equal
<> | not equal (removed in python3)
() | function calls and tuples
[] | lists
{} | dictionary {key:value} & set {value}
@ | 
, |
: |
. |
= | assignment operator
; | end statement/expression
+= | add to variable
-= | subtract from variable
\*= | multiply variable
/= | divide variable
//= | divide and floor variable
%= | divide and assign remainder to variable
\*\*= | exponantiate variable
