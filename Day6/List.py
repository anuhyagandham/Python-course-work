Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=[1,2,3,4,5,6,7]
l
[1, 2, 3, 4, 5, 6, 7]
type(l)
<class 'list'>
#properties
l.append(12)
l
[1, 2, 3, 4, 5, 6, 7, 12]
l.append(6)
l
[1, 2, 3, 4, 5, 6, 7, 12, 6]
id(l)
2185864793024
l.append(3)
l
[1, 2, 3, 4, 5, 6, 7, 12, 6, 3]
id(l)
2185864793024
l=[2,'python',3.4,5+6j,[1,3,5],(2,4,6),{1,2,3,4},{1:1,2:2}]
l
[2, 'python', 3.4, (5+6j), [1, 3, 5], (2, 4, 6), {1, 2, 3, 4}, {1: 1, 2: 2}]
names=['anu','priya','kavitha']
girls=['sarayu','alekhya']
name+girls
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name+girls
NameError: name 'name' is not defined. Did you mean: 'names'?
names+girls
['anu', 'priya', 'kavitha', 'sarayu', 'alekhya']
girls*3
['sarayu', 'alekhya', 'sarayu', 'alekhya', 'sarayu', 'alekhya']
names[0]
'anu'
names[::2]
['anu', 'kavitha']
s=names+girls
s
['anu', 'priya', 'kavitha', 'sarayu', 'alekhya']
s[::2]
['anu', 'kavitha', 'alekhya']
s[1:2:1]
['priya']
s[1::2]
['priya', 'sarayu']
s[::-1]
['alekhya', 'sarayu', 'kavitha', 'priya', 'anu']
'anu' in names
True
'vasu' in names
False
'anu' not in s
False
s
['anu', 'priya', 'kavitha', 'sarayu', 'alekhya']
sorted(s)
['alekhya', 'anu', 'kavitha', 'priya', 'sarayu']
sorted(s,reverse)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sorted(s,reverse)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
sorted(s,reverse=True)
['sarayu', 'priya', 'kavitha', 'anu', 'alekhya']
max(s)
'sarayu'
min(s)
'alekhya'

s
['anu', 'priya', 'kavitha', 'sarayu', 'alekhya']
s[1]='chandini'
s
['anu', 'chandini', 'kavitha', 'sarayu', 'alekhya']
s.append('anuhya')
s
['anu', 'chandini', 'kavitha', 'sarayu', 'alekhya', 'anuhya']
s.insert(1,'priya')
s
['anu', 'priya', 'chandini', 'kavitha', 'sarayu', 'alekhya', 'anuhya']
s.pop()
'anuhya'
s
['anu', 'priya', 'chandini', 'kavitha', 'sarayu', 'alekhya']
s.pop(2)
'chandini'
s
['anu', 'priya', 'kavitha', 'sarayu', 'alekhya']
s.remove('anu')
s
['priya', 'kavitha', 'sarayu', 'alekhya']
del s[1]
s
['priya', 'sarayu', 'alekhya']
s.clear()
s
[]
>>> l=[1,2,3,4,5,1,1,3,4,5,6]
>>> l
[1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6]
>>> l.index(3)
2
>>> l.count(1)
3
>>> l.index(6)
10
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6, 5]
>>> m=l
>>> m.append(4)
>>> l
[1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6, 5, 4]
>>> m
[1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6, 5, 4]
>>> k=[1,2,3]
>>> n=k.copy()
>>> n
[1, 2, 3]
>>> n.append(4)
>>> n
[1, 2, 3, 4]
>>> l
[1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6, 5, 4]
>>> k
[1, 2, 3]
>>> k.reverse()
>>> k
[3, 2, 1]
>>> sum(k)
6
>>> any([1,2,3,0,0,0])
True
>>> any([0,0,0])
False
>>> any([(),,0,0,0])
SyntaxError: invalid syntax
>>> any([(),0,0,0])
False
>>> all([1,2,3])
True
>>> all([0,0,0])
False
