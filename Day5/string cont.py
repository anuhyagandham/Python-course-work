Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
s
'python programming'
s.startswith('py')
True
s.startswith("ja")
False
s.endswith("ing")
True
s.endswith("on")
False
'abc'.isalpha()
True
'a12b'.isalpha()
False
'abc def'.isalpha()
False
'12345'.isnumeric()
True
'a12s3'.isnumeric()
False
'a123cd'.isalnum()
True
>>> 'abbc'.isalnum()
True
>>> '112233'.isalnum()
True
>>> 'abcd 12345'.isalnum()
False
>>> 'abcd_12345'.isalnum()
False
>>> True'abcd 12345'.isalnum()
SyntaxError: invalid syntax
>>> 'abcd12345'.isalnum()
True
>>> 'abcd 12345'.isalnum()
False
>>> 'abcd_12345'.isalnum()
False
>>> 'abc'.isupper()
False
>>> 'ABC'.isupper()
True
>>> 'abc'.islower()
True
>>> 'hello   world'.isspace()
False
>>> '      '.isspace()
True
>>> 'Abc Xyz'.istitle()
True
>>> 'AAb Xyz'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> '3456'.isdigit()
True
>>> 'abcd'.isdigit()
False
>>> '1234'.isdecimal()
True
>>> 'abcde'.isdecimal()
False
>>> '3456'.isdigit()
True
>>> '3456.345'.isdigit()
False
>>> '3456'.isdigit()
True
