Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d[1]='int'
d[2.34]='float'
d['string']='str'
d[3+4j]='complex'
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3)]='tuple'
d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
s[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[{1:1,2:2}]='dict'
NameError: name 's' is not defined
d
{1: 'int', 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple'}
d[1]='integer'
>>> d
{1: 'integer', 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple'}
>>> d[1]=1
>>> d[2]=3.45
>>> d[3]='str'
>>> d[4]=[1,2,3]
>>> d[5]=(1,2,3)
>>> d[6]={1,2,3}
>>> d[7]={1:1,2:2}
>>> d[8]=1+2j
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: (1+2j)}
>>> d[3]
'str'
>>> d[6]
{1, 2, 3}
>>> d[12]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d[12]
KeyError: 12
>>> d.get(12,'Key not present')
'Key not present'
>>> d.get(1,'Key not present')
1
>>> d.get(5,'Key not present')
(1, 2, 3)
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: (1+2j)}
>>> d[4]=8
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: 8, 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: (1+2j)}
>>> d[8]=4
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: 8, 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: 4}
>>> d[9]=10
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: 8, 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: 4, 9: 10}
>>> d.update({10:11,11:12})
>>> d
{1: 1, 2.34: 'float', 'string': 'str', (3+4j): 'complex', (1, 2, 3): 'tuple', 2: 3.45, 3: 'str', 4: 8, 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 1, 2: 2}, 8: 4, 9: 10, 10: 11, 11: 12}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
