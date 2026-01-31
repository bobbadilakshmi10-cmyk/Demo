#list comprehension
'''a=["codegnan","python","course"]
#[["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())
b=str(a)
c=b.upper()
print(c)

for i in a:
    print(i.upper(), end=" ")

#syntax:
    #a=[expr for var in collections/range]
a=[i.upper() for i in a]
print(a)'''

#task
'''a=["vja","vzg","bng"]
a=[i.title() for i in a]
print(a)

a=[1,2,4,5,6,8,12,13]
a=[i*i for i in a]
a=[i**2 for i in a]
a=[pow(i,2) for i in a]
print(a)'''

#if-usage in list compreshension
'''a=[i for i in range(16) if i%2==0]
print(a)

a=[i*i for i in range(16) if i%2==0]
print(a)

a=["apple","mango","banana","kiwi","berry","dragan"]
a=[i for i in a if "a" in i]
print(a)

a=["apple","mango","banana","kiwi","berry","dragan"]
a=[i for i in a if "a" not in i]
print(a)'''

#if-else list compreshension
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)



