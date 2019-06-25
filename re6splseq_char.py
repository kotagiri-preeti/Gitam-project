#special sequences and characcters
import re
str='hello world'
x=re.findall("he..o",str)   #mathces any character except new line
print(x)
x1=re.findall("^hello",str) #matches the strat of the string
print(x1)
x2=re.findall("ld$",str)    #matches the end of the string or just before new line at the end of the string
print(x2)
str1 = "The rain in Spain falllls mainly in the plain !"
x = re.findall("al{2,3}", str1) #matches exactly 2 occurences of 'l'
print(x)
str2="the rain in spain"
str3="hello 123 "
print(re.findall(r"\bain",str2))    #available at the begining  of the word
print(re.findall(r"ain\b",str2))    #available at the end of the word
print(re.findall(r"\Bain",str2))    #available but not at the begining  of the word
print(re.findall(r"ain\B",str2))    #available but not at the end of the word
print(re.findall(r"\Athe",str2))    #available at the begining of the string
print(re.findall("\d",str3))    #match for digits
print(re.findall("\D",str3))    #other than digits
print(re.findall("\s",str3))    #spaces
print(re.findall("\w",str3))    #words-->a-z , A-Z,0-9
print(re.findall("\W",str3))    #other than words

