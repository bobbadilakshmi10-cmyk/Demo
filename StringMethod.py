Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Method
#len
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count('twinkle")
        
SyntaxError: unterminated string literal (detected at line 1)
a.count("twinkle")
        
2
a.count("t")
        
5
a.count("1")
        
0
a.count(" ")
        
3
#Find String
        
a="code"
        
a[2]
        
'd'
a.find("d")
        
2
a.find("e")
        
3
b="codegnan"
        
b.find("n")
        
5
b[5]+b[7]
        
'nn'
#escape Sequence
        
#\n-new line
        
#\t-tab space
        
a="name\nmobile\tmailid\ncity"
        

print(a)
        
name
mobile	mailid
city
b="name:lakshmi\nmobileno:545454252\tmailid:lakshmi@gmail.com\tcity:vij"\
        print(b)
        
SyntaxError: invalid syntax
b="name:lakshmi\nmobileno:545454252\tmailid:lakshmi@gmail.com\tcity:vij"
        
print(b)
        
name:lakshmi
mobileno:545454252	mailid:lakshmi@gmail.com	city:vij
#replace
        
a="Work until you succeed"
        
a.replace("wait","work")
        
'Work until you succeed'
#upper()
        
a="hello"
        
a.upper()
        
'HELLO'
#lower()
        
a.lower()
        
'hello'
#Capitalize()
        
a="python"
        
a.capitalize()
        
'Python'
b="python Course"
        
b.tittle()
        
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
b.title()
        
'Python Course'
c="i am in class"
        
c.title()
        
'I Am In Class'
a="python"
        
a.startwith("p")
        
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.startwith("p")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("p")
        
True
a.endswith("n")
        
True
a.isupper()
        
False
a.islower()
        
True
a.isdigit()
        
False
b=3456
        
b.isdigit()
        
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="3456"
        
b.isdigit()
        
True
a="hello word"
        
a.isalpha()
        
False
b="helloworld"
        
a.isalpha()
        
False
b.isalpha()
        
True
c="pooja123"
        
c.isalnum()
        
True
d="pooja"
        
d.isalnum()
        
True
#strip()
        
a="   lakshmi    "
        
a.lstrip()
        
'lakshmi    '
a.rstrip()
        
'   lakshmi'
a.strip()
        
'lakshmi'
#split()
        
a="python java c c++"
        
a.split()
        
['python', 'java', 'c', 'c++']
b="i am learning python course"
        
b.split()
        
['i', 'am', 'learning', 'python', 'course']
#join()
        
a="python","java","ml"
        
"".join(a)
        
'pythonjavaml'
" ".join(a)
...         
'python java ml'
>>> 'python java ml'
...         
'python java ml'
>>> 
>>> #concatenation
...         
>>> a="code"
...         
>>> b="gnan"
...         
>>> print(a+b)
...         
codegnan
>>> a="python"
...         
>>> b="cporse"
...         
>>> print(a+" "+b)
...         
python cporse
>>> fname="lakshmi"
...         
>>> lname="b"
...         
>>> print(fname.title()+" "+lname.title())
...         
Lakshmi B
>>> print(fname+lname().title())
...         
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print(fname+lname().title())
TypeError: 'str' object is not callable
>>> print(fname+" "+lname).title())
SyntaxError: unmatched ')'
>>> print((fname+" "+lname).title())
Lakshmi B
