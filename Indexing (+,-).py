Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
#Positive
a="vijayawada"
a[0]
'v'
a[1]
'i'
a[0]+a[1]+a[2]+a[3]
'vija'
a="I love python"
a[0]
'I'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'I love'
a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
#Negative
b="work until you succeed"
a[-21]+a[-20]+a[-19]+a[-18]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[-21]+a[-20]+a[-19]+a[-18]
IndexError: string index out of range
b[-21]+b[-20]+b[-19]+b[-18]
'ork '
b[-17]+b[-16]+b[-15]+b[-14]+b[-13]
'until'
#Silicing
#Positive
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[:4]
'code'
a[4:8]
'gnan'
a[4:]
'gnan'
a="Beautiful is better than ugly"
a[0:9]
'Beautiful'
a[13:19]
'better'
a[25:29]
'ugly'
#Negative Silicing
a="Time is very precious"
a[-21]+a[-20]+a[-19]+a[-18]
'Time'
>>> a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]
'preciou'
>>> #striding
>>> #[a]Indexing
>>> #[a:b]silicing
>>> #[a:b:c]-striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::2]
'dt cec'
>>> a[::1]
'data science'
>>> b="cloud computing"
>>> a[::6]
'dc'
>>> a[::3]
'dacn'
>>> a[::4]
'd e'
>>> a[5:9]
'scie'
>>> b[::6]
'cci'
>>> a[::3]
'dacn'
>>> a[::4]
'd e'
>>> b[::3]
'cucpi'
>>> b[::4]
'cdmi'
>>> b[4:9]
'd com'
>>> b[:6]
'cloud '
>>> b[8:]
'mputing'
