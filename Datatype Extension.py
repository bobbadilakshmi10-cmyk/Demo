Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int
int(4)
4
int(5.8)
5
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(8+2j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(8+2j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(Fals)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(Fals)
NameError: name 'Fals' is not defined. Did you mean: 'False'?
int(Fale)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(Fale)
NameError: name 'Fale' is not defined. Did you mean: 'False'?
int(False)
0
#float
float(4.5)
4.5
float(5)
5.0
float("hi")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(4+2j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(4+2j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
>>> float(False)
0.0
>>> #String
>>> str(5)
'5'
>>> str(4.5)
'4.5'
>>> str("hello")
'hello'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(5)
(5+0j)
>>> complex(4.5)
(4.5+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(5)
True
>>> bool(6.7)
True
>>> bool("hello")
True
>>> bool(True)
True
>>> bool(False)
False
