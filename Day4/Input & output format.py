Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
anu
name
'anu'
name=input('Enter your name : ')
Enter your name : anu
name
'anu'
age=int(input())
age
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    age=int(input())
ValueError: invalid literal for int() with base 10: 'age'
21
21
age
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    age
NameError: name 'age' is not defined
age=int(input())
21
age
21
gpa=float(input())
9.1
gpa
9.1

names=list(input('names: ').split())
names: anu vasu anuhya vasavi
names
['anu', 'vasu', 'anuhya', 'vasavi']

names=tuple(input('names: ').split())
names: anu vasu anuhya vasavi
names
('anu', 'vasu', 'anuhya', 'vasavi')

names=set(input('names: ').split())
names: anu vasu anuhya vasavi
names
{'anu', 'vasu', 'vasavi', 'anuhya'}

marks=list(map(int,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
[45, 54, 64, 75, 65]

marks=tuple(map(int,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
(45, 54, 64, 75, 65)

marks=set(map(int,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
{64, 65, 75, 45, 54}

marks=list(map(float,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
[45.0, 54.0, 64.0, 75.0, 65.0]

KeyboardInterrupt
marks=tuple(map(float,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
(45.0, 54.0, 64.0, 75.0, 65.0)

marks=set(map(float,input('marsks: ').split()))
marsks: 45 54 64 75 65
marks
{64.0, 65.0, 75.0, 45.0, 54.0}

a=eval(input().split())
a
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
a=eval(input('Enter').split())
Enter2
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a=eval(input('Enter').split())
TypeError: eval() arg 1 must be a string, bytes or code object
a
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=eval(input().split())
23
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
anuhya
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    anuhya
NameError: name 'anuhya' is not defined
e=eval(input('enter: '))
enter: 23
e
23
type(e)
<class 'int'>
e=eval(input('enter: '))
enter: anu
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    e=eval(input('enter: '))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'anu' is not defined. Did you mean: 'any'?
e=eval(input('enter: '))
enter: 45.6
e
45.6
type(e)
<class 'float'>

e=eval(input('enter: '))
enter: 'anuhya'
e
'anuhya'
type(e)
<class 'str'>

e=eval(input('enter: '))
enter: [1 2 3 4]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    e=eval(input('enter: '))
  File "<string>", line 1
    [1 2 3 4]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?


e=eval(input('enter: '))
enter: [1,2,3,4,5]
e
[1, 2, 3, 4, 5]
type(e)
<class 'list'>

e=eval(input('enter: '))
enter: (1,2,3,4)
e
(1, 2, 3, 4)
type(e)
<class 'tuple'>

e=eval(input('enter: '))
enter: {1,2,3,4}
e
{1, 2, 3, 4}
type(e)
<class 'set'>

id,pd=input('Enter the id pd : ').split())
SyntaxError: unmatched ')'
id,pd=input('Enter the id pd : ').split()
Enter the id pd : anu anu@23
id
'anu'
pd
'anu@23'

a,b,c=list(map(int,input('enter: ').split()))
enter: 23 24 25
a
23
b
24
c
25
a,b,c
(23, 24, 25)



a='python'
b=23
c=45.6
print(a,b,c)
python 23 45.6
print('a=',a,'b=',b,'c=',c)
a= python b= 23 c= 45.6
print('a=',a,'b=',b,'c=',c,sep='')
a=pythonb=23c=45.6
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
python
b=
23
c=
45.6
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	python	b=	23	c=	45.6
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
python
b=

... 23
c=
45.6

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	python	b=	23	c=	45.6
>>> print('a=',a,'b=',b,'c=',c,end='\n\n\n')
a= python b= 23 c= 45.6


>>> print('a=',a,'b=',b,'c=',c,end='@@@')
a= python b= 23 c= 45.6@@@
>>> 
>>> 
>>> print(f'a={a} b={b} c={c}')
a=python b=23 c=45.6
>>> 
>>> print(f'a={2} b={0} c={1}')
a=2 b=0 c=1
>>> print(f'a={a} b={b} c={c}')
a=python b=23 c=45.6
>>> print('a= %s b= %d c= %f'.%(a,b,c))
SyntaxError: invalid syntax
>>> print('a= %s b= %d c= %f',%(a,b,c))
SyntaxError: invalid syntax
>>> print('a= %s b= %d c= %f'%(a,b,c))
a= python b= 23 c= 45.600000
>>> print('a= {} b= {} c= {}'.format(a,b,c))
a= python b= 23 c= 45.6
>>> print('a= {2} b= {0} c= {1}'.format(a,b,c))
a= 45.6 b= python c= 23
