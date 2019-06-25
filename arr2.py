from array import *
val=array('l',[12,34,56])
x=int(input("enter the element to search"))
for i in range(len(val)):
    if val[i]==x:
        print(i)
else:
    print("element not found")
    