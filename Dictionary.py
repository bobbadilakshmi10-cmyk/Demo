Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"Lakshmi","year":22026,"month":1}
print(a)
{'name': 'Lakshmi', 'year': 22026, 'month': 1}
type(a)
<class 'dict'>
b={"name","year","Month"}
type(b)
<class 'set'>
#Keys
a={"name":"lakshmi","year":2026,"month":1}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['lakshmi', 2026, 1])
#accesing
a={"name":"lakshmi","city":"vij"}
a["name"]
'lakshmi'
a["city"]
'vij'
a["vij"]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a["vij"]
KeyError: 'vij'
#update()
a={"date":23,"day":"fri","time":10}
a.update({"year":2026"})
          
SyntaxError: unterminated string literal (detected at line 1)
a.update({"year":2026})
          
a
          
{'date': 23, 'day': 'fri', 'time': 10, 'year': 2026}
a.update({"month":2,"min":27})
          
a
          
{'date': 23, 'day': 'fri', 'time': 10, 'year': 2026, 'month': 2, 'min': 27}
#Setdefault()
          
a={"course":"python"}
          
a.setdefault("codegnan","Institue")
          
'Institue'
a
          
{'course': 'python', 'codegnan': 'Institue'}
#pop{}
          
a={"food":"Biriyani","fruits":""mango"}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"food":"Biriyani","fruits":"mango"}
   

a
   
{'food': 'Biriyani', 'fruits': 'mango'}
a.pop()
   
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop('food')
   
'Biriyani'
a
   
{'fruits': 'mango'}
a.popitem()
   
('fruits', 'mango')
a={"name":"lakshmi","mailid":"blakshmi10@gmail.com"}
   
a.copy()
   
{'name': 'lakshmi', 'mailid': 'blakshmi10@gmail.com'}
>>> a.count("name")
...    
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a.clear()
...    
>>> a
...    
{}
>>> a={"year":2026,"month":2,"date":23}
...    
>>> a.get("year")
...    
2026
>>> a={"name":"lakshmi","age":22,"name":"lakshmi"}
...    
>>> print(a)
...    
{'name': 'lakshmi', 'age': 22}
>>> a={"name":"lakshmi","age":22,"name":"Bhanu"}
...    
>>> a
...    
{'name': 'Bhanu', 'age': 22}
>>> a={"name":"lakshmi","age":22,"name1":"lakshmi"}
...    
>>> a
...    
{'name': 'lakshmi', 'age': 22, 'name1': 'lakshmi'}
>>> a={"idnos":[20,30,40],"name":["lakshmi","bhanu","sudha"]}
...    
>>> print(a)
...    
{'idnos': [20, 30, 40], 'name': ['lakshmi', 'bhanu', 'sudha']}
>>> a.keys()
...    
dict_keys(['idnos', 'name'])
>>> a.values()
...    
dict_values([[20, 30, 40], ['lakshmi', 'bhanu', 'sudha']])
>>> type(a)
...    
<class 'dict'>
