Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuples()
>>> a=(4.5.7,"python",4+9j,True,False)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=(4,5.7,"python",4+9j,True,False)
>>> print(a)
(4, 5.7, 'python', (4+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count("python")
1
>>> a.index(True)
4
