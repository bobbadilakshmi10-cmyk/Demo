#modules
'''def greetings(name):
    print("name is",name)'''

'''a=3
b=6
print("the sum is:",a+b)'''

details={"names":["lakshmi","bhanu","sudha"],"places":["vij","vzg","hyd"]}

if __name__=="__main__":
    a=[10,20,30,40,50]
    #a.append("code")
    a.extend("code")
    print(a)

'''[10, 20, 30, 40, 50, 'code']
[10, 20, 30, 40, 50, 'c', 'o', 'd', 'e']#script'''

def dummy():
    if __name__=="__main__":
        print("this program is run as script")#script in run
    else:
        print("this program is run as module")
dummy()

'''this program is run as script'''
