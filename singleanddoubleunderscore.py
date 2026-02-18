#difference between _and__
'''class Employee():
    def __init__(self):
        self.name="lakshmi"
        self._mailid="lakshmi10@gmai.com"
        self.__salary=10000#private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)error
print(a._Employee__salary)

lakshmi
lakshmi10@gmai.com
10000'''

'''class employee():
    def __init__(self):
        self.name="bhavani"
        self._mailid="bhanu@gmail.com"
        self.__salary=12000
class employee1():
    def __init__(self):
        self.name="sudha"
        self._mailid="sudha@gmail.com"
        self.__salary=12000
b=employee()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._employee__salary)
b=employee1()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._employee1__salary)'''

#Polymorphism
#operator overloading
'''a=2;b=5
print(a+b)
print(a.__add__(b))
print(a.__add__(4))
print(a.__sub__(1))
print(a.__mul__(5))
print(a.__pow__(2))
#prin(a.__div__(2))
print(a.__ge__(1))
print(a.__le__(10))
a=[1,2,3,4,5,6];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))#concatination
print(a.__add__(" "+b))
print("code".__add__("gnan"))

7
7
6
1
10
4
True
True
[1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
4
10
codegnan
code gnan
codegnan'''


#operator overriding
class A():
    def __init__(self,a):
        self.a=a
    def __sub__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)
y=B(6)
#x=4
#y=6
print(x-y)

24
    
