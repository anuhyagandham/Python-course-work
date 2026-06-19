Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python program'
s
'python program'
fname='Anuhya'
lname='gandham'
fname+lname
'Anuhyagandham'
n='anu vasu siri'
n[0]
'a'
n[2]
'u'
n[-1]
'i'
n[:5]
'anu v'
n[5:]
'asu siri'
n[-1:-6:-1]
'iris '
n[-7:-10]
''
n[-6:-9]
''
n[-14:]
'anu vasu siri'
n[1::2]
'n ausr'
n
'anu vasu siri'
len(n)
13
'anu' in n
True
'babu' in n
False
n
'anu vasu siri'
len(n)
13
ord(a)#asci value
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ord(a)#asci value
NameError: name 'a' is not defined
ord(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord('a')
97
ord('A')#asci value
65
chr(40)
'('
n=
SyntaxError: invalid syntax
n
'anu vasu siri'
sorted(n)
[' ', ' ', 'a', 'a', 'i', 'i', 'n', 'r', 's', 's', 'u', 'u', 'v']
max(n)
'v'
min(n)
' '
' '
' '
chr(97)
'a'
n.upper()
'ANU VASU SIRI'
n.lowe()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    n.lowe()
AttributeError: 'str' object has no attribute 'lowe'. Did you mean: 'lower'?
n.lower()
'anu vasu siri'
n.capitalize()
'Anu vasu siri'
n.swapcase()
'ANU VASU SIRI'
n
'anu vasu siri'
n.Capitalize()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    n.Capitalize()
AttributeError: 'str' object has no attribute 'Capitalize'. Did you mean: 'capitalize'?
n.capitalize()
'Anu vasu siri'
s.title()
'Python Program'
n.title()
'Anu Vasu Siri'
n.center(60,"*")
'***********************anu vasu siri************************'
n.ljust(60,'_')
'anu vasu siri_______________________________________________'
n.rjust(60,'_')
'_______________________________________________anu vasu siri'
'60'.zfill(4)
'0060'
'100'.zfill(5)
'00100'
n.zfill(67)
'000000000000000000000000000000000000000000000000000000anu vasu siri'
'000000000000000000000000000000000000000000000000000000anu vasu siri'
'000000000000000000000000000000000000000000000000000000anu vasu siri'
n.find('a')
0
n.find('b')
-1
n.find(i)
       
SyntaxError: unterminated string literal (detected at line 1)
n.find('i')
       
10
n.rfind('i')
       
12
n.rfind('u')
       
7
n.find('u')
       
2
n.index('a')
       
0
n.index('i')
       
10
n.rindex('i')
       
12
n.index('b')
       
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    n.index('b')
ValueError: substring not found
n.count('a')
       
2
n.count('i')
       
2
n.split()
       
['anu', 'vasu', 'siri']
n.split(2)
       
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    n.split(2)
TypeError: must be str or None, not int
n.split('',2)
       
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    n.split('',2)
ValueError: empty separator
n.split(' ',2)
       
['anu', 'vasu', 'siri']
n.split('-',2)
       
['anu vasu siri']
n.rsplit(' ',2)
       
['anu', 'vasu', 'siri']
n.splitlines()
       
['anu vasu siri']
n.partition('a')
       
('', 'a', 'nu vasu siri')
n.partition('v')
       
('anu ', 'v', 'asu siri')
n.rpartition('v')
       
('anu ', 'v', 'asu siri')
n.joint('')
       
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    n.joint('')
AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
s=['multi','line','comment']
       
''.join(s)
       
'multilinecomment'
'-'.join(s)
       
'multi-line-comment'
n.strip()
       
'anu vasu siri'
n.rstrip()
       
'anu vasu siri'
n,lstrip()
       
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    n,lstrip()
NameError: name 'lstrip' is not defined
n.lstrip()
       
'anu vasu siri'
n='    Hello World     '
       
n.strip()
       
'Hello World'
n.rstrip()
       
'    Hello World'
n.lstrip()
       
'Hello World     '
s
       
['multi', 'line', 'comment']
>>> s='python program'
...        
>>> s
...        
'python program'
>>> s.replace('python','java')
...        
'java program'
>>> s
...        
'python program'
>>> s.maketrans("aeiou","*****")
...        
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
>>> s.translate(s.maketrans("aeiou","*****"))
...        
'pyth*n pr*gr*m'
>>> 'pyth*n pr*gr*m'
...        
'pyth*n pr*gr*m'
>>> s
...        
'python program'
>>> m
...        
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    m
NameError: name 'm' is not defined
>>> n
...        
'    Hello World     '
>>> n='Hello World'
...        
>>> n
...        
'Hello World'
>>> n='hello world 😀'
...        
>>> n.encode()
...        
b'hello world \xf0\x9f\x98\x80'
>>> b'hello world \xf0\x9f\x98\x80'.decode()
...        
'hello world 😀'
s='python programming'
s
       
