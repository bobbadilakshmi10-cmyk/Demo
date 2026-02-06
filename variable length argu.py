#variable length arguments:
'''def check(*a):
    print(a)
    print(type(a))
check()

check(2,3,4,5,6)
b=[2,3,4,5,6]
check(*b)

check(2,3,4,5,6)
c={2,3,4,5,6}
check(*c)

check(2,3,4,5,6)
d={"year":2026,"name":"lakshmi"}
check(*d)

check(2,3,4,5,6)
c=(2,3,4,5,6)
check(*c)

#for in using variable length
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6,)
check1(2,3,4,5,6,2.3,4.2)
check1(2,3,4,5,2.3,4.5)

def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
          d=d+i
        print(d)
check1()
check1(2,3,4,5,6,)
check1(2,3,4,5,6,2.3,4.2)
check1(2,3,4,5,2.3,4.5,"lakshmi")'''

#kewards(**)
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],"name":["lakshmi","bhanu","sudha"],"places":["vij","vzg","hyd"]}
Details(**d)

def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
        for i in a.values():
            print(i)
            for i in a:
                print(i,a[i])
d={"idnos":[10,20,30],"name":["lakshmi","bhanu","sudha"],"places":["vij","vzg","hyd"]}
Details()'''

#both * and **usage:
'''def final(*a,**b):
    d=1#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
final()'''

def final(*a,**b):
    d=1#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
        for i,j in b.items():
            print("key is",i)
            print("values is",j)
final()
data=(2,3,4,5,6,7,4.2)
final(*data)
details={"idnos":[10,20,30],"name":["lakshmi","bhanu","sudha"],"places":["vij","vzg","hyd"]}
final(**details)
final(*data,**details)

            
            



