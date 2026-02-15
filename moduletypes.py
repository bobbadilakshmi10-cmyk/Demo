Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#math module
import math
math.pi
3.141592653589793
math.pi*3
9.42477796076938
math.sqrt(2)
1.4142135623730951
math.log(2)
0.6931471805599453
math.tan(45)
1.6197751905438615
math.cos(60)
-0.9524129804151563
math.sin(30)
-0.9880316240928618
math.pow(2,3)
8.0
math.pow(2,4)
16.0
from math import pi,sqrt,log,tan
pi
3.141592653589793
sqrt(4)
2.0
tan(45)
1.6197751905438615
log(10)
2.302585092994046
math.pi
3.141592653589793
#sys module
import sys
sys.path
['', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\idlelib', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314\\python314.zip', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314\\DLLs', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314\\Lib', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314', 'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages']
for i in sys.path:
    print(i)

    

C:\Users\bobba\AppData\Local\Programs\Python\Python314\Lib\idlelib
C:\Users\bobba\AppData\Local\Programs\Python\Python314\python314.zip
C:\Users\bobba\AppData\Local\Programs\Python\Python314\DLLs
C:\Users\bobba\AppData\Local\Programs\Python\Python314\Lib
C:\Users\bobba\AppData\Local\Programs\Python\Python314
C:\Users\bobba\AppData\Local\Programs\Python\Python314\Lib\site-packages
sys.version
'3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]'
import os
os.path
<module 'ntpath' (frozen)>
os.getcwd()
'C:\\Users\\bobba\\AppData\\Local\\Programs\\Python\\Python314'
os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python314.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
os.mkdir("feb13")
os,listdir()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    os,listdir()
NameError: name 'listdir' is not defined
>>> os.listdir()
['DLLs', 'Doc', 'feb13', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python314.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> ['DLLs', 'Doc', 'feb13', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python314.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
['DLLs', 'Doc', 'feb13', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python314.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> 
>>> math.ceil(4.8)
5
>>> math.celi(11.15)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    math.celi(11.15)
AttributeError: module 'math' has no attribute 'celi'
>>> math.ceil(6,7)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.ceil(6,7)
TypeError: math.ceil() takes exactly one argument (2 given)
>>> math.ceil(11.15)
12
>>> #floor
>>> math.floor(5.9)
5
>>> math.fllor(0.4)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    math.fllor(0.4)
AttributeError: module 'math' has no attribute 'fllor'. Did you mean: 'floor'?
>>> math.floor(0.4)
0
