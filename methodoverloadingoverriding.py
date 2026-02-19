#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends...")
x=new()
x.sum()
x.sum(2,3,5)
x.sum(6,3)

program ends...
the sum is 10
product is 18'''

#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sound")
class Dog():
    def speak(self):
        print("barks")
a=Animal()
b=Dog()
a.speak()
b.speak()

animals can make sound
barks'''

#inheritance
#single inheritance
'''class RBI():#parent class
    cash=100000
    @classmethod
    def avaliable_cash(self):
        print("avaliable_cash is",self.cash)
        print("avaliable_cash is",RBI.cash)
class SBI(RBI):#child class 1
    pass
class HDFC(RBI):
    cash=50000
    @classmethod
    def new_cash(self):
        print("new cas is",self.cash+self.cash)
        print("new cash is",self.cash+RBI.cash)
a=HDFC()
a.avaliable_cash()
a.new_cash()

avaliable_cash is 50000
avaliable_cash is 100000
new cas is 100000
new cash is 150000'''

'''class vechiles():
    def driving(self):
        print("driving the car")
class bike():
    def driving(self):
        print("driving the bike")
a=vechiles()
b=bike()
a.driving()
b.driving()'''

#Multiple inheritence
'''class Father():
   def height(self):
       print("height is 5.5 inches")
class Mother():
    def weight(self):
        print("weight is 60 kgs")
class Kid():
    def dob(self):
        print("just Born....")
a=Father()
a.height()
b=Mother()
b.weight()
c=Kid()
c.dob()

height is 5.5 inches
weight is 60 kgs
just Born....'''

'''class Father():
   def height(self):
       print("height is 5.5 inches")
class Mother():
    def weight(self):
        print("weight is 60 kgs")
class Kid(Father,Mother):
    def dob(self):
        print("just Born....")
a=Kid()
a.height()
a.weight()
a.dob()

height is 5.5 inches
weight is 60 kgs
just Born....'''

#Multilevel inheritance
class grand_parent():
    def land(self):
        print("land is 1 lack")
class parent(grand_parent):
    def house(self):
        print("house is 50k")
class child(parent):
    def vechile(self):
        print("vechile")
a=child()
a.land()
a.house()
a.vechile()

land is 1 lack
house is 50k
vechile




