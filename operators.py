Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a%b)
4
print(a**b)
4096
#Assignment
a=3
b=5
a+=b
b+=a
print(a)
8
b-=a
print(b)
5
b*=a
print(b)
40
b//=a
print(b)
5
b/=a
print(b)
0.625
b%=a
print(b)
0.625
b**=a
print(b)
0.023283064365386963

#comparision
a=4
b=9
a>b
False
b<b
False
B<a
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    B<a
NameError: name 'B' is not defined. Did you mean: 'b'?
b<a
False
a!=b
True
a==b
False
a<=b
True
a>=b
False
#Logical
a=3
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True
#Identify
a=6
if type(a) is int:
...     print("it is int")
... 
...     
it is int
>>> if type(a) is not int:
...     print("False")
... 
...     
>>> #Membership
...     
>>> a=1,2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 20 in a:
...     print(20)
... 
...     
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> a=6,8,9,3,4,6,1,4,12
>>> if 8 in a
SyntaxError: expected ':'
>>> if 8 in a:
...     print("true")
... 
...     
true
>>> a="python","java","c"
>>> if "python" in a:
...     print("true")
... 
...     
true
