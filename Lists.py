Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=4.5
type(b)
<class 'float'>
c=[5.6]
type(c)
<class 'list'>
#List methods
a=["python","java","c"]
a.appent("c++")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.appent("c++")
AttributeError: 'list' object has no attribute 'appent'. Did you mean: 'append'?
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","car")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","car")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","car"])
a
['python', 'java', 'c', 'c++', ['ml', 'car']]
#extend
a=["vij","vzg","hyd"]
a.extend("bng","chennai")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.extend("bng","chennai")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["bng","chennai"])
a
['vij', 'vzg', 'hyd', 'bng', 'chennai']
#insert
a=["ds","ai","ml"]
a.insert(1,"python")
a
['ds', 'python', 'ai', 'ml']
a.insert(3,"c++")
a
['ds', 'python', 'ai', 'c++', 'ml']
#index
a=["apple","bannana","kiwi"]
a.index("bannana")
1
#sort
b=["apple","bannana","kiwi","grapes",berry"]
   
SyntaxError: unterminated string literal (detected at line 1)
b.sort()
   
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b.sort()
AttributeError: 'float' object has no attribute 'sort'
b=["apple","bannana","kiwi","grapes","berry"]
   
b.sort()
   




c=["apple","kiwi","bannan"]
   
c.sort()
   
c
   
['apple', 'bannan', 'kiwi']
d=5,6,8,9,3
   
d.sort()
   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d.sort()
AttributeError: 'tuple' object has no attribute 'sort'
d=[3,6,8,90,2,4]
   
d.sort()
   
d
   
[2, 3, 4, 6, 8, 90]
#reverse()
   
a=["hi",,"hello","how","are","you"]
   
SyntaxError: invalid syntax
a.reverse()
   
a
   
['kiwi', 'bannana', 'apple']
#pop()
   
a=["java","python","c","ds"]
   
a.pop()
   
'ds'
a.pop(1)
   
'python'
a
   
['java', 'c']
a.pop("c")
   
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.pop("c")
TypeError: 'str' object cannot be interpreted as an integer
#Remove()
   
a=["lakshmi","bhanu","sudha"]
   
a.remove("bhanu")
   
a
   
['lakshmi', 'sudha']
#copy()
   
a.copy()
   
['lakshmi', 'sudha']
b=a.copy()
   
b
   
['lakshmi', 'sudha']
#clear()
   
a.clear()
   
a
   
[]
b=[]
   
b.append("lakshmi")
   
b
   
['lakshmi']
#len()
   
a=["css","java","c++"]
   
len(a)
   
3
b="css"
   
>>> len(b)
...    
3
>>> d=["css"]
...    
>>> len(d)
...    
1
>>> #count()
...    
>>> a=["red","white","green"]
...    
>>> a.count("green")
...    
1
>>> a.count("red","green")
...    
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.count("red","green")
TypeError: list.count() takes exactly one argument (2 given)
>>> a=["c","c++","java"]
...    
>>> a.extend([""python","ml"])
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> a.extend(["python',"ml"])
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> a.extend(["python","ml"])
...           
>>> a
...           
['c', 'c++', 'java', 'python', 'ml']
>>> a.extend("dsa")
...           
>>> a
...           
['c', 'c++', 'java', 'python', 'ml', 'd', 's', 'a']
