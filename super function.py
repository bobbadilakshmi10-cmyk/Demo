#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
obj1=child("bhanu",22)
print(obj1.name)
print(obj1.age)

parent constructor
child constructor
bhanu
22


#bulit in functions
print(),sum(),len(),max(),min(),range(),pow(),type(),dir(),input()'''

#fromkeys()
a="codegnan"
print(a)
print(list(a))
print(set(a))
print(tuple(a))
#print(dict(a))

b=dict.fromkeys(a)
print(a)

c=dict.fromkeys(a,"pooja")
print(c)

c=["c"]="hello"
print(c)


#eval()function
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)


a=float(input("a value"))
b=float(input("b value"))
print(a+b)

a=input("a value"))
b=input("b value"))
print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

'''a value12
b value2
14
a value2.4
b value2
4.4
a valueTrue
b valueTrue
2
a valueTrue
b valueFalse
1
a value"lakshmi"
b value"bhanu"
lakshmibhanu'''

#enumerate()
names=["lakshmi","bhanu","sudha rani","mery","isreal"]
for i in range(len(names)):
    print(i,names[i])

a=dict(enumerate(names))
print(a)

a=dict(enumerate(names,100))
print(a)

a=list(enumerate(names))
print(a)

'''0 lakshmi
1 bhanu
2 sudha rani
3 mery
4 isreal
{0: 'lakshmi', 1: 'bhanu', 2: 'sudha rani', 3: 'mery', 4: 'isreal'}
{100: 'lakshmi', 101: 'bhanu', 102: 'sudha rani', 103: 'mery', 104: 'isreal'}
[(0, 'lakshmi'), (1, 'bhanu'), (2, 'sudha rani'), (3, 'mery'), (4, 'isreal')]'''


#zip function
a=[10,20,30,40,50]
names=["lakshmi","geethika","isha","halle","bhanu"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

[10, 20, 30, 40, 50, 'lakshmi', 'geethika', 'isha', 'halle', 'bhanu']
<zip object at 0x00000263B9FDDB00>
[(10, 'lakshmi'), (20, 'geethika'), (30, 'isha'), (40, 'halle'), (50, 'bhanu')]
((10, 'lakshmi'), (20, 'geethika'), (30, 'isha'), (40, 'halle'), (50, 'bhanu'))
{(30, 'isha'), (50, 'bhanu'), (10, 'lakshmi'), (40, 'halle'), (20, 'geethika')}
{10: 'lakshmi', 20: 'geethika', 30: 'isha', 40: 'halle', 50: 'bhanu'}


    
