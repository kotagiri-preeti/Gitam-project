import re
phone="1234-567-890 # phone number"
str1="preethi 1234 20000 9999999999"
num=re.sub('\D',"",phone)
print("phone number:",num)
print(re.split("\s",str1,2))