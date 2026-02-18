#oops Syntax
'''class classname():
    name="lakshmi"
    age=20
    city="vij"
    def fname(self):
        print(statement...)
a=classname()
a.fname()'''

#class declaration
'''class details():
    name="lakshmi"
    age=21
    city="vzg"
    def display(self):
        print(self.name,self.age,self.city)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("lakshmi",25,"vij")
a.display()
b=details()
b.data("bhane",24,"vzg")
b.display()

lakshmi 25 vij
bhane 24 vzg'''

#object initialization
'''class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("lakshmi",25,"vij")
a.display()
a=details("bhanu",24,"vij")
a.display()'''

'''class details():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.city=input("city")
    def display(self):
        print(self.name,self.age,self.city)
a=details()
a.display()'''

class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(input("name"),int(input("age")),input("city"))
a.display()


        

