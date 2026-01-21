Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#farmating
a=10
b=20
print(a+b)
30
print("the sum is",a+b)
the sum is 30
print("the sum is, a+b")
the sum is, a+b
city="vij"
print("the city is",city)
the city is vij
#farmat
a="lakshmi"
>>> b="bhanu"
>>> print("hello {}{}".format(a,b))
hello lakshmibhanu
>>> print("hello {} {}".formate(a,b))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("hello {} {}".formate(a,b))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print("hello {} {}".format(a,b))
hello lakshmi bhanu
>>> print("hello {} hello {}".format(a,b))
hello lakshmi hello bhanu
>>> a="sudha"
>>> b="siva"
>>> print(f"hello {a} {b}")
hello sudha siva
>>> print(f"hello {a} hello {b}")
hello sudha hello siva
>>> #farmatting #farmat #fstring
>>> a=3
>>> b=7
>>> c=a*b
>>> 
>>> print("the product is {}".format())
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("the product is {}".format())
IndexError: Replacement index 0 out of range for positional args tuple
>>> print("the product is{c}")
the product is{c}
>>> print("the product is {}".format(a*b))
the product is 21
>>> print(f"the product is {a*b}")
the product is 21
>>> a="lakshmi"
>>> print(a[:4])
laks
>>> a[4:]
'hmi'
