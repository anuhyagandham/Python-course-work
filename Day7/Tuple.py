Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,1,1)
t
(1, 1, 1)

(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
t=(1,2,3,4,5,6)
t*3
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
t=(1,2,3,4,6,2,4,8,6,9)
t.index(3)
2
t.count(6)
2
t[:3]
(1, 2, 3)
t[8:12]
(6, 9)
t[::-1]
(9, 6, 8, 4, 2, 6, 4, 3, 2, 1)
min(t)
1
max(t)
9
any((1,2,3))
True
all((7,8))
True
all((5,7))
True
all((0,1))
False
any(0,1,2,3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    any(0,1,2,3)
TypeError: any() takes exactly one argument (4 given)
any((0,1,2,3))
True
>>> 7 in t
False
>>> 8 in t
True
>>> 6 not in t
False
>>> 5 not in t
True
>>> t=(1,3.45,"string",[1,2,3,4],(1,2,3),{2,3,4},{2:3,4:5})
>>> t
(1, 3.45, 'string', [1, 2, 3, 4], (1, 2, 3), {2, 3, 4}, {2: 3, 4: 5})
>>> t(3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
>>> t[3]
[1, 2, 3, 4]
>>> t[3].append(5)
>>> t
(1, 3.45, 'string', [1, 2, 3, 4, 5], (1, 2, 3), {2, 3, 4}, {2: 3, 4: 5})
>>> t=(1,2,3,4,6,2,4,8,6,9)
>>> sum(t)
45
>>> len(t)
10
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> t=(1,2,3,4)
>>> w,x,y,z=t
>>> w
1
>>> x
2
>>> y
3
>>> z
4
>>> t=(1,2,3,4,6,2,4,8,6,9)
>>> sorted(t)
[1, 2, 2, 3, 4, 4, 6, 6, 8, 9]
