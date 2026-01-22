Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Sets{}
a={3,4.5,"python",5+9j,True,False}
print(a)
{False, True, (5+9j), 3, 4.5, 'python'}
type(a)
<class 'set'>
a={4,8,9,2,3,9,4}
print(a)
{2, 3, 4, 8, 9}
#subset()
a={1,2,3,6,7,8,9}
b={1,2,3,7}
b.subset(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.subset(a)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
b.issubset(a)
True
a.issubset(b)
False
#Superset()
a={4,6,7,8,9,10}
b={8,9,10}
a.issuperset(b)
True
b.issuperset(a)
False
#unions(
0
0
)
SyntaxError: unmatched ')'
#Union()
a={1,2,3,4,5,6,7}
b={4,8,5,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 10}
#intersection()
a={1,2,3,4,5,6,7}
b={1,2,3,4}
a.intersection(b)
{1, 2, 3, 4}
#difference()
a={1,2,4,5,6,7,8}
b={1,2,5,6,7,3,10}
a.difference(b)
{8, 4}
b.difference(a)
{10, 3}
#Updates()
a={1,2,3,4,5,6,7}
b={2,1,5,6,8,9,10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Symentric
_difference()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    _difference()
NameError: name '_difference' is not defined
#symentric_difference()
a={20,40,50,60,70}
b={20,40,80,90}
a.symetric_difference(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.symetric_difference(b)
AttributeError: 'set' object has no attribute 'symetric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{70, 80, 50, 90, 60}
b.symmetric_difference(a)
{80, 50, 70, 90, 60}
#difference_update()
a={1,2,3,4,5}
b={4,5,6,7,8,9}
a.difference_update(b)

b.difference_update(a)

b
{4, 5, 6, 7, 8, 9}
a
{1, 2, 3}
#intersection-update()
a={1,2,3,4,5}
b={3,4,5,6,7,8,9}
a.intersection_update(b)
a
{3, 4, 5}
b.intersection_update(a)
b
{3, 4, 5}
#Symentric_difference_updates()
a={1,2,3,4,5,6}
b={5,1,2,3,4,7,9,10}
a.symmetric_difference_update(b)
a
{6, 7, 9, 10}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 5, 6}
#pop()
a={3,4,5,6,7}
b={1,2,3,4,8,9}
a.pop()
3
a
{4, 5, 6, 7}
a.pop(6)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
a.remove(6)
a
{4, 5, 7}
#copy()
a={1,2,3,4,5}
a.copy()
{1, 2, 3, 4, 5}
b=a.copy()
b
{1, 2, 3, 4, 5}
#clear()
a={1,4,5,6,7}
a.clear()
a
set()
b=set()
b.add(30)
b
{30}
#len()
a={3,5,6,7,8,9}
len(a)
6
a.count(6)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.count(6)
AttributeError: 'set' object has no attribute 'count'
#discard()
>>> a={1,2,3,4}
>>> a.discard(1)
>>> a
{2, 3, 4}
>>> #isdisjoint()
>>> a={2,3,4,5,67}
>>> b{2,3,4,5,9}
SyntaxError: invalid syntax
>>> b={2,3,4,5,9,8}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
>>> #task()
>>> a={9,1,5,2,8,4,6,3,7,0]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.index[8,6,5,7,9,9,4,2,3,1]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.index[8,6,5,7,9,9,4,2,3,1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.index(1)
1
>>> a.append()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> a.pop()
9
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8]
