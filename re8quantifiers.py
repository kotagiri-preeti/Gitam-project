import re 
#str1="hello everyone.he is abc.he is doing job"
str2="ggg gg"
#print(re.findall('he', str1))
#print(re.findall('he*', str1))
#print(re.findall('he+', str1))
#print(re.findall('hello?', str1))
print(re.findall('g*', str2))   #matches 0 or more repitions of pattern
print(re.findall('g+', str2))   #match the longest text even if parts of matching text also match
print(re.findall('g?', str2))   #matches the shortest part of test with pattern.



