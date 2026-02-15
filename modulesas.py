Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #ASCII
... #CHR()
... chr(80)
'P'
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> chr("a")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    chr("a")
TypeError: 'str' object cannot be interpreted as an integer
>>> chr(30)
'\x1e'
>>> #ord()
>>> ord("a")
97
>>> ord("z")
122
>>> ord(97)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord(97)
TypeError: ord() expected string of length 1, but int found

'''for i in range(65,91):
    print(chr(i),end=" ")

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'''

for i in range(97,123):
    print(chr(i),end=" ")

a b c d e f g h i j k l m n o p q r s t u v w x y z 



name=input("enter the name")
for i in name:
    print(i,"_",ord(i))
