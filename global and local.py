#first case of global variable
'''a=3
def check():
    print("inside value is:",a)
check()
print("outside value is:",a)

inside value is: 3
outside value is: 3

#second case of global variable:
a=4
def check1():
    a=6
    a=a**2
    print("inside value is:",a)
check1()
print("outside value is:",a)

inside value is: 36
outside value is: 4'''

#third case of both global and local variables:
'''a=4
b=7
def check2():
    a=5
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13#local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)

inside value is 5
updated value is 15
value of b is 23
a value is 4
b value is 7'''

#usage of global keyword:
'''a=8
def final():
    global a,b #a,b keywords
    print("inside value is",a)
    a=4
    print("updated value is",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)

inside value is 8
updated value is 4
value of b is 19
a value is 4
b value is 19'''

#generaters
#a=[exp for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
<class 'list'>'''

'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))'''

'''<generator object <genexpr> at 0x0000024E1D0A8E10>
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
<class 'generator'>'''


'''a=(i for i in range(21))
print(a)
print(list(a))
print(type(a))'''

'''<generator object <genexpr> at 0x0000022874B0B6B0>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
<class 'generator'>'''

'''a=(i for i in range(21))
print(a)
print(set(a))
print(type(a))'''

''' <generator object <genexpr> at 0x0000027C5A6E8E10>
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
set()'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))

enter the values3,12
3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))

enter the values3,12
4'''

#diff b/w yield and return
def mygen():
    #return "python"
    #return "c"
    #return "java"
    return "python","java","c"
print(*mygen())

python java c

#yield
'''def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())'''

#next()
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration'''
    

