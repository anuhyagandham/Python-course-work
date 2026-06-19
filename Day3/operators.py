Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=23
a=23
b=10
a+b
33
a-b
13
a*b
230
a/b
2.3
a//b
2
a**b
41426511213649
a**2
529
------
SyntaxError: invalid syntax
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True

a += 17
a
40
a-=10
a
30
a*=2
a
60
a//=2
a
30
a**=2
a
900
a%=2
a
0
a+=40
a
40
a/=2
a
20.0
a//=0
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a//=0
ZeroDivisionError: division by zero
a//=1
a
20.0
a//=2
a
10.0
a/=1
a
10.0

s='python'
s[0]=='p'
True
s[-1]=='n'
True
s[0]=='p' and s[-1]=='n'
True

s='python prgm'
s[0]=='p' or s[-1]=='n'
True
s[-1]=='n'
False
not s[-1]=='n'
True

s
'python prgm'
'py' in s
True
'ja' not in s
True
l=['air','bag','phn','desk']
'air' in l
True
'phone' not in l
True
t=(2,3,6,9,8)
2 in t
True
4 not in t
True
6 not in t
False
d={'name':'anu','batch': 56, 'age': 21}
'name' in d
True
'anu' in d
False
56 in d
False
'batch' in d
True
s={6,18,36,42}
6 in s
True
8 not in s
True
8 in s
False

l=[1,2,3,4]
m=[1,2,3,4]
l==m
True
l is m
False
n=m
n
[1, 2, 3, 4]
n==m
True
n is m
True
l is m
False
id(l)
1836617649408
id(n)
1836617778240
id(m)
1836617778240
n is m
True
n is not m
False
l is not m
True
l is m
False
n is m
True

11&12
8
11|12
15
11^12
7
~11
-12
~12
-13
12<<2
48
12>>2
3
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> 
>>> f=3.14
>>> int(f)
3
>>> complex(f)
(3.14+0j)
>>> str(f)
'3.14'
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
>>> set(f)]
SyntaxError: unmatched ']'
>>> set(f)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
>>> list(f)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
>>> TypeError: 'float' object is not iterable
SyntaxError: invalid syntax
>>> 
