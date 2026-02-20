#Encapsulation
#publicdata()
'''class parent():
    publicdata=10
    def publicmethod1(self):
        print(self.publicdata)
class child(parent):
    def publicmethod2(self):
        print(self.publicdata)
obj1=child()
obj1.publicmethod1()
obj1.publicmethod2()

10
10'''

#_protcteddata
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class chiled(parent):
    def method2(self):
        print(self._protecteddata)
obj1=chiled()
obj1.method1()
obj1.method2()

100
100'''

#privatedata
'''class parent():
    __privatedata="pooja"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()

class A():
    def method1(self):
        print("hello")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data")
obj1=A()
obj1.method1()#error output'''

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("it is 2 implimentation")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("it is 1 implimentation")
    def method3(self):
        print("it is 3 implimentation")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()

it is 1 implimentation
it is 2 implimentation
it is 3 implimentation



'''ticket=1000
gender=input("choose the gender")
age=int(input("enter the age"))
if gender=="m":
    if age>=60:
        print("senior citizen")
        ticket=ticket-30/100*ticket
        print(ticket)
    elif age<60:
        print("normal citizen")
        print(ticket)
    elif gender=="f":
        if age>=60:'''
