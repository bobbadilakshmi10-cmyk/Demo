#keyword and positional arguments:
'''def Details(id,name,mailid):
    id=10
    name="lakshmi"
    mailid="lakshmi10@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")

def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="bhanu",mailid="bhanu@gmail.com")
details(id=30,name="hani",mailid="hani@gmail.com")
'''datails(40,"rani","rani@gmail.com")
details("rani","rani@gmail.com",60)'''
details(mailid="chandu@gmail.com",id=60,name="chandu")'''

#default arguments
'''def grocery(item,price):
    print("itme is %s" %item)
    print("price is %" 2f"%price)
grocery("sugar",100)

def grocery(item="rice",price=1500):
      print("itme is %s" %item)
      print("price is % 2f" %price)
grocery()

def grocery(item,price=200):
      print("itme is %s" %item)
      print("price is % 2f "%price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non-def follows def arg
      print("itme is %s" %item)
      print("price is %,2f" %price)
grocery(500)'''


'''#cake,price qty
def items(cake,price,qty):
    print("cake is %s"%cake)
    print("price is %d"%price)
    print("qty is %s"%qty)
items("chocolate",100,"1")'''

#* arguments:is used unpack elements
'''a=[2,3,4,5,6]
print(a)
print(*a)

a=(4,5,6,7)
print(a)
print(*a)

a={3,4,5,6}
print(a)
print(*a)

a={"year":2026,"month":2}
print(a)
print(*a)

a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)#error

a,b,c=2,3,4
print(a)
print(b)
print(c)

*a,b,c=2,3,4,5,6,7,8
print(*a)
print(b)
print(c)

a,*b,c=2,3,4,5,6,7,8
print(a)
print(*b)
print(c)

a,b,*c=2,3,4,5,6,7,8
print(a)
print(b)
print(*c)

a="codegnan"
print(a)
print(*a)

a,b,c="codegnan"
print(a)
print(b)
print(c)#error

a,b,c="codegnan"
print(*a)
print(b)
print(c)

a,b,c="cod"
print(a)
print(*b)
print(c)

a,b,c="cod"
print(a)
print(b)
print(*c)'''








