import re
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
x1=re.findall("xyz",str)
print(x1)
print(re.sub(" ","*",str))
print(re.split(" ",str))
print(re.split(" ",str,1))
p=re.compile('in')
m=p.finditer(str)
print(m)
#x1=re.finditer("in",str)
for i in m:
    print(i)
x = re.findall("in", str)
print(x)
print(re.sub("-","","123-456-7891"))
