Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,5,5}
s
{1, 2, 3, 4, 5}
s={1,4,6,89,34,23,67}
s
{1, 34, 67, 4, 6, 23, 89}
34 in s
True
7 not in s
True
89 in s
True
s.add(1)
s.add(2.34)
s.add(3+4j)
s.add((1,2,3))
s.add(False)
s
{False, 1, 2.34, 67, 4, 6, (3+4j), 23, 89, 34, (1, 2, 3)}
girls={'anu','priya','sarayu','kavitha','alekhya'}
boys={'madhav','sairam','bharath','vamsi','ravi'}
topper={'madhav','sairam'}
girls | boys
{'sairam', 'priya', 'madhav', 'bharath', 'ravi', 'sarayu', 'alekhya', 'vamsi', 'anu', 'kavitha'}
girls &boys
set()
boys&topper
{'madhav', 'sairam'}
boys-girls
{'sairam', 'madhav', 'bharath', 'ravi', 'vamsi'}
boys-topper
{'ravi', 'vamsi', 'bharath'}
boys^topper
{'ravi', 'vamsi', 'bharath'}
a={1,2,3,4,5}
{1,2}>=a
False
{1,2,3,4,5,6,7,8,9}>=a
True

girls
{'kavitha', 'sarayu', 'priya', 'anu', 'alekhya'}
boys
{'ravi', 'sairam', 'madhav', 'vamsi', 'bharath'}
girls.disjoint(boys)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    girls.disjoint(boys)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
girls.isdisjoint(boys)
True
girls.union(boys)
{'sairam', 'priya', 'madhav', 'bharath', 'ravi', 'sarayu', 'alekhya', 'vamsi', 'anu', 'kavitha'}
girls.add('anuhya')
girls.update('chandini','vasavi')
girls
{'d', 'priya', 'sarayu', 'v', 'kavitha', 'n', 'anuhya', 'i', 'h', 'a', 'c', 's', 'anu', 'alekhya'}
girls
{'d', 'priya', 'sarayu', 'v', 'kavitha', 'n', 'anuhya', 'i', 'h', 'a', 'c', 's', 'anu', 'alekhya'}
>>> girls={'kavitha', 'sarayu', 'priya', 'anu', 'alekhya'}
>>> girls
{'kavitha', 'sarayu', 'priya', 'anu', 'alekhya'}
>>> girls.add('anuhya')
>>> girls
{'kavitha', 'sarayu', 'priya', 'anuhya', 'anu', 'alekhya'}
>>> girls.update({'chadini','vasavi'})
>>> girls
{'kavitha', 'sarayu', 'priya', 'chadini', 'vasavi', 'anuhya', 'anu', 'alekhya'}
>>> boys.pop()
'ravi'
>>> boys
{'sairam', 'madhav', 'vamsi', 'bharath'}
>>> boys.pop()
'sairam'
>>> boys
{'madhav', 'vamsi', 'bharath'}
>>> boys.remove('vamsi')
>>> boys
{'madhav', 'bharath'}
>>> boys.discard('vamsi')
>>> boys.discard('bharath')
>>> boys
{'madhav'}
>>> boys.clear()
>>> boys
set()
>>> max(girls)
'vasavi'
>>> min(girls)
'alekhya'
>>> len(girls)
8
>>> sorted(girls)
['alekhya', 'anu', 'anuhya', 'chadini', 'kavitha', 'priya', 'sarayu', 'vasavi']
>>> f=frozenset({1,2,3,3,4,5})
>>> f
frozenset({1, 2, 3, 4, 5})
>>> sum(f)
15
>>> min(f)
1
>>> max(f)
5
>>> 
