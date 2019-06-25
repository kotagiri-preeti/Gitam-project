def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("1.addition\n2.substraction\n3.multiplication\n4.division")
sel=int(input("enter the selection number"))
if(0<sel<=4 ):
    a=int(input("enter the value for a"))
    b=int(input("enter the value for b"))
if sel==1:
    print(add(a,b))
elif sel==2:
    print(sub(a,b))
elif sel==3:
    print(mul(a,b))
elif sel==4:
    print(div(a,b))
else:
    print("selected operation is not valid")