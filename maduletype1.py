#random module
'''import random
a=random.sample(range(10,40),21)
print(a)

[24, 39, 26, 37, 36, 16, 19, 15, 10, 20, 31, 11, 14, 38, 22, 27, 34, 30, 17, 35, 21]'''

#randint()
'''import random
a=random.randint(3,10)
print(a)

4 randomly printed'''

#choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

'''import random
while True:
    input("roll of Dies")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("stop")

roll of Dies4
1
roll again?(y/n)y
roll of Dies6
3
roll again?(y/n)n'''

    





