import re
str1="the rain in spain  rain"
z=re.match("THE",str1,re.I)
print(z)
x=re.search("rain", str1)
print(x)
y=re.findall("rain", str1)
print(y)
print("first white space is at:",x.start())
print("first white space ending is at:",x.end())
print("first white space start and end is at:",x.span())
y=re.search("portugal",str1)
print(y) 