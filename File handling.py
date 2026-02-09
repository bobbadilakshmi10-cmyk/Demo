#file handling
#write
'''a=open("lakshmi.txt","w")
a.write("codegnan it solutions")
a.close()

a=open("lakshmi.txt","w")
a.write("python")
a.close()

#append()
a=open("lakshmi.txt","a")
a.write("java")
a.close()

a=open("lakshmi.txt","w")
b=input("enter the data:")
a.write(b)
a.close()

a=open("lakshmi.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("lakshmi.txt","w")
a.write(input("data"))
a.close()'''

#readline()
'''a=open("lakshmi.txt")
#print(a.read())# it will display entire content
#print(a.readline())#it will display first line
#print(a.read(10))#it will display number of charcters
#print(a.readlines())#it will with \n'''

#writelines()#it makes every object side by side
'''a=open("python.txt","w")
b=["bhanu","sudha","nageswararao","sivakumar","lucky"]
a.writelines(b)
#a.writelines("\n".join(b))
a.close()'''

a=open("Atm Application.py")
print(a.read())

a=open("C:\\Users\\bobba\\Desktop\\Function.py")
print(a.read())

#Error Handling
#syntax error
'''for i in range(10)#syntax error
    print(i)'''

#Run time error()
a=int(input("a value"))
b=int(input("b value"))
print(a+b)

#logical error()
a=10
b=20
print(a-b)

a=15
b=30
if a<b:
    print("true")

a=15
b=30
if a>b:
    print("true")#not visible
    
   
