'''num =int(input("enter the number:"))
for i in range(1, 11):
    print(num,"x",i,"=",num*i)'''

'''print("----Expense Tracker-----")
username=input("enter the username:")
category=input("enter the category:")
amount=int(input("enter the amount:"))
print("-----Summary---")
print("name",username)
print("category name",category)
print("amount spended",amount)'''


'''print("---------Calculator By Using Functions------")
def add(a,b):
    print(a+b)
def sub(a,b):
   print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("the addition",add(a,b))
print("the sub is",sub(a,b))
print("the mul is",mul(a,b))
print("the div is",div(a,b))'''

#marks analyzer
marks=[]
count=int(input("enter the total no.of students"))
for i in range(count):
    mark=int(input("enter the marks:"))
    marks.append(mark)
print("\n marks entered")
for j in marks:
    print(j)
height=max(marks)
lowest=min(marks)
total=sum(marks)
average=total/len(marks)
print("-----marks analyzer----")
print("display height:",height)
print("display lowest:",lowest)
print("display total:",total)
print("display average:",average)



enter the total no.of students5
enter the marks:80
enter the marks:20
enter the marks:10
enter the marks:40
enter the marks:60

 marks entered
80
20
10
40
60
-----marks analyzer----
display height: 80
display lowest: 10
display total: 210
display average: 42.0
