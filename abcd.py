import fun1
print(fun1.addition(1,2,3,4))
try:
    abcd()
except NameError as e:
    print("something went wrong i.e:",e)
    
def abcd():
    print("hello")