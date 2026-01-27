#conditions
#if-elifconditions
'''a=6
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")'''

'''a=5
b=7
if a==b:
    print("less")
elif a<b:
    print("greater")
elif a!=b:
    print("not equal")'''

#if-elifconditions Logical operator
#And Or Not
''''a=20
b=30
if a>b and a<b:
    print("false")
elif a<b or b>a:
    print("True")
elif not a<b and b>=a:
    print("true")'''

#identifier operator:
'''a=4
if type(a) is not int:
    print("true")
elif type(a) is int:
    print("false")'''

#member ship operator:
'''a=1,2,3,4,5
if 6 in a:
    print("true")
elif 2 in a:
    print("false")'''

#if-elif-else conditions:

'''a=20
b=30
if a>b:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")'''

#logical operators if-elif-else conditions:
'''a=2
b=3
if a>b and b>a:
    print("true")
elif a>b or b>a:
    print("false")
elif not a>b and b>=a:
    print("true")
else:
        print("true")'''
#identifier operator:
'''a=2,3,4,5,6,7
if type(a) is not int:
    print("false")
elif type(a) is int:
    print("true")
else:
    print("false")'''

#membership operator:
'''a=1,2,3,4,5
if 6 in a:
    print("false")
elif 7 in a:
    print("false")
else:
    print("true")'''

#multiple-if:
'''a=3
b=5
if a<b:
    print("true")
if b>a:
    print("True")'''
#Logical operator
'''a=6
b=7
if b<a and b>a:
    print("true")
if a>b or b>a:
    print("True")
if not a>b and b>a:
    print("True")'''

#identifier
''''a=30,20,40,50,60
if type(a) is int:
    print("true")
if type(a) is not int:
    print("False")'''

#Membership
'''a=2,3,4,5,6
if 2 in a:
    print("True")
if 7 in a:
    print("false")'''

#Nested-if
'''a=5
b=6
if a<b:
    print("true")
    if b>a:
        print("True")'''

'''a=7
b=8
if a==b:
    print("true")
    if a>b:
         print("false")
    else:
        print("true")'''

'''a=6
b=7
if a==b:
    print("true")
    if b>a:
        print("true")
    elif a!=b:
        print("greater")
else:
    print("True")'''

#voting
#task age=18:
'''age=int(input("enter the age"))
if age>=18:
    print("elgible for vote")
else:
    print("not elgible")'''

#even or odd
'''number=int(input("enter the number"))
if number%2==0:
    print("enter even number")
else:
    print("it is odd")'''
#welcome name or welcome guest
'''name=input("enter the name").title()
if name=="Lakshmi":
    print("Welcome",name)
else:
    print("welcome guest")'''

#5 names

'''names=["lakshmi","bhanu","sudha","rani","pooja"]
name=input("enter the name")
if name in names:
    print("welcome",name)
else:
    print("welcome guest")'''

'''task1 social media:nested if 
    username=lakshmi
    password=1234
task2:leap year 2024 if else
not leap year 2026'''

#task1
'''name=input("username")
password=input("password")
if name=="lakshmi":
    if password=="1234":
        print("sucess")
else:
    print("not sucess")'''

#task2:

'''num=int(input("enter leaf year"))
if num%2024==0:
    print("leap year")
else:
    print("not leap year")'''

years=[2024,2028,2032]
num=int(input("enter the number"))
if num in years:
    print("leap year",num)
else:
    print("Not leap year")
    
    
        



    
    
    
