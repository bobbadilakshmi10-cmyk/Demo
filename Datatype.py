Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5
type(a)
<class 'int'>
b=4.5
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
c="course"
type(c)
<class 'str'>
d='''codegnan'''
type(d)
<class 'str'>
e=4+8j
type(e)
<class 'complex'>
>>> f=2j+9
>>> print(f)
(9+2j)
>>> g=2j
>>> type(g)
<class 'complex'>
>>> x=j
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x=j
NameError: name 'j' is not defined
>>> j=j
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    j=j
NameError: name 'j' is not defined
>>> y=j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    y=j
NameError: name 'j' is not defined
>>> h=2j
>>> type(h)
<class 'complex'>
>>> i=True
>>> type(i)
<class 'bool'>
>>> j=False
>>> type(j)
<class 'bool'>
>>> i=true
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    i=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> i="true"
>>> type(i)
<class 'str'>
