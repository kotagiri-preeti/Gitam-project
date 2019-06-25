import re
str1 = "The rain in Spain"
'''y = re.search("Portugal", str1)
print(y)
y = re.match("Portugal", str1)
print(y)
y = re.search("in", str1)
print(y)
y = re.match("in", str1)
print(y)
y = re.search("The", str1)
print(y)'''
y = re.match("THE", str1,re.I)
print(y)
print(re.split("\s",str1,1))
print(re.sub("\s","*",str1))
print(re.findall('in',str1))
print(re.search('rain*',str1).group())