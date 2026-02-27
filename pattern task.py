'''r=int(input("enter the number:"))
c=int(input("enter the number:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i*j,end=" ")
    print()

enter the number:5
enter the number:5
1 2 3 4 5 
2 4 6 8 10 
3 6 9 12 15 
4 8 12 16 20 
5 10 15 20 25 '''

'''r=int(input("enter the number:"))
c=int(input("enter the number:"))
for i in range(r):       
    for j in range(1,c+1):
        print(j,end=" ")
    print()
    
enter the number:2
enter the number:3
1 2 3 
1 2 3 '''


'''r=int(input("enter the number:"))
c=int(input("enter the number:"))
for i in range(1,r+1):
    for j in range(1,c):
        print(i,end=" ")
    print()

enter the number:3
enter the number:4
1 1 1 
2 2 2 
3 3 3

1 2 3
4 5 6
7 8 9'''

'''n=1
for i in range(3):
    for j in range(3):
        print(n,end=" ")
        n+=1
    print()

1 2 3 
4 5 6 
7 8 9 '''

'''n=1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()

1 
2 3 
4 5 6 
7 8 9 10 


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


1 
1 2 
1 2 3 
1 2 3 4 '''




