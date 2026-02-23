#write a function to calculate 2*x+5 wherx=5
'''def calculate():
    x = 5
    answer= 2 * x + 5
    return answer
print(calculate())

def calculate():
    x=int(input("value"))
    print(2*x+5)
calculate()

#annonymous functions
#syntax:
#a=lambda are:expr
a=lambda x:2*x+5
print(a(5))

a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(5,4))

a=int(input("a value"))
b=int(input(" b value"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a="codegnan"
upper=lambda x:x.upper()
print(upper(a))

a="python course"
title=lambda x:x.title()
print(title(a))'''

a="lakshmi"
b="bobbadi"'''
a=lambda x,y:x+" "+y.title()
print(a("lakshmi","bobbadi"))'''

'''a,b=[input(x) for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''#filter()
a=[10,20,35,47,50,60,80,87,83,100]
if a%2==0:
    print(a)#error

for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda x:x%2==0,a))
print(b)

b=list(filter(lambda x:x%2!=0,a))
print(b)

#[],(),{},set()
a=[]
print(type(a))
a=()
print(type(a))
a={}
print(type(a))
a=set()
print(type(a))

a=[[],(),set(),{},"",None,3,6.7,"python",7+9j,True,False]
b=list(filter(None,a))
print(b)

10
20
50
60
80
100
[10, 20, 50, 60, 80, 100]
[35, 47, 87, 83]
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
[3, 6.7, 'python', (7+9j), True]'''

#map()
'''a=[2,5,7,9,11,15,20,30]
b=[1,3,6,13,20,40,60,80]
c=list(map(max,a,b))
print(c)

[2, 5, 7, 13, 20, 40, 60, 80]

d=list(map(min,a,b))
print(d)

[1, 3, 6, 9, 11, 15, 20, 30]

a=input("name1:")
b=input("name2:")
print(a+b)

a,b=input("enter the names").split(",")
print(a+b)

a,b=[x for x in input("enter the names").split(",")]
print(a+b)

a=int(input("a value:"))
b=int(input("b value:"))
print(a+b)

a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values")).split(",")
print(a+b)#error

a,b=map(int,input("enter the values").split(","))
print(a+b)

a,b=map(str,input("enter the values").split(","))
print(a+b)

b=list(map(int,input("enter the values").split(",")))
print(b)

b=tuple(map(int,input("enter the values").split(",")))
print(b)

b=set(map(int,input("enter the values").split(",")))
print(b)'''

b = dict(map(lambda x: x.split(":"),
             input("Enter key:value pairs: ").split(",")))
print(b)


    
    
