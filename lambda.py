total=0 #global variable
def sum(arg1,arg2):
    total=arg1+arg2     #local variable
    print("inside total:",total)
sum(10,20)
print("outside total:",total)

