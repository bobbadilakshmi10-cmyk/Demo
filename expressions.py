#regular Expression
'''a="codegnan is in vijayawada"
print(a)

a="codegnan\nis\tin\nvij"
print(a)

#rstring
a=r"codegnan\nis\tin\nvij"
print(a)

#compile(),search(),findall(),split(),sub()
#sequence charcters
\w-it matches alphanumaric
\W-it matches non-alphanumaric
\d-it matchs any digits
\D-it matches non digits
\s-it represents white spaces
\S-it represents non white spaces'''

#compile()
import re
a="maths map cat code cash money mat cap dog donkey"
b=re.compile(r"m\w\w\w\w")
print(b)

#re.compile('m\\w\\w\\w\\w')

#search()
'''c=b.search(a)
print(c)

#<re.Match object; span=(0, 5), match='maths'>

d=re.search(r"m\w+",a)
print(d)

#<re.Match object; span=(0, 5), match='maths'>

#findall()
e=re.findall(r"m\w+",a)
print(e)

#['maths', 'map', 'money', 'mat']
f=re.findall(r"m\w+",a)
print(*f)#unpack string

#maths map money mat

g=re.findall(r"c\w+",a)
print(g)

#['cat', 'code', 'cash', 'cap']

h=re.findall(r"d\w+",a)
print(h)

#['de', 'dog', 'donkey']

#split()
x=re.split(r"m\w",a)
print(x)

['', 'ths ', 'p cat code cash ', 'ney ', 't cap dog donkey']

ye=re.split(r"\s",a)
print(ye)

['maths', 'map', 'cat', 'code', 'cash', 'money', 'mat', 'cap', 'dog', 'donkey']
z=re.split(r"\S",a)
print(z)

['', '', '', '', '', ' ', '', '', ' ', '', '', ' ', '', '', '', ' ', '', '', '', ' ', '', '', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', '', '', '', '']

#sub()
d=re.sub(r"maths","science",a)
print(d)

#science map cat code cash money mat cap dog donkey
h=re.sub(r"m","k",a)
print(h)

kaths kap cat code cash koney kat cap dog donkey'''

'''import re
a="year 2026 month 2 date 16"
b=re.compile(r"m\w\w\w\w")
print(b)

h=re.findall("\d+",a)
print(h)

s=re.findall("\D+",a)
print(s)'''

weight=float(input("enter the weight kgs:"))
height=float(input("enter the height in meters:"))
bmi = round(weight / (height ** 2), 2)
if bmi<18.5:
     print("under weight")
elif 18.5<= bmi<25:
    print("heavy weight")
elif 25 <= bmi < 30:
    print("over weight")
else:
    print("obesity")



