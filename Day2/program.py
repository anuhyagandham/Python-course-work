Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
myvar=10
my var=10
SyntaxError: invalid syntax
Myvar=10
9myvar
SyntaxError: invalid decimal literal
_myvar
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    _myvar
NameError: name '_myvar' is not defined. Did you mean: 'myvar'?
-myvar=10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a=b=c=10
a
10
b
10
c
10
a,b,c=10,20,30
a
10
b
20
c
30
a,b=b,a
a
20
b
10
10
10

   
a=10
type(a)
<class 'int'>
a=10.50
type(a)
<class 'float'>
a=9+10X
SyntaxError: invalid decimal literal
c=2+9j
type(c)
<class 'complex'>
c=2+9j














s="python"

s="python"
s
'python'
type(s)
<class 'str'>
s=s+'lang'
s
'pythonlang'

id(s)
2552053815472
s=s+'prgm'
id(s)
2552019322096

li=[1,2,3,31,1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> li=[1,2,3,1,2]
>>> li
[1, 2, 3, 1, 2]
>>> id(li)
2552056170368
>>> li.append(20)
>>> li
[1, 2, 3, 1, 2, 20]
>>> id(li)
2552056170368
>>> 
>>> t=(1,2,3,4,231,87,2)
>>> t
(1, 2, 3, 4, 231, 87, 2)
>>> type(t)
<class 'tuple'>
>>> 
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> type(s)
<class 'set'>
>>> s={236376,35768,1298,236376}
>>> s
{236376, 1298, 35768}
>>> 
>>> d={'name':'kavitha','batch':'56'}
>>> d
{'name': 'kavitha', 'batch': '56'}
>>> type(d)
<class 'dict'>
>>> 
>>> 
>>> boolean
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    boolean
NameError: name 'boolean' is not defined
>>> payment_status=Ture
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    payment_status=Ture
NameError: name 'Ture' is not defined
>>> payment_status=True
>>> status=False
