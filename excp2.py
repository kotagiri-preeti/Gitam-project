a=int(input("enter value of a"))
b=int(input("enter value of b"))
try:
    print(a/b)
    print(c)
except (ZeroDivisionError,TypeError,NameError):
    print("something wrong")
#except TypeError as e:
 #  print("something wrong",e)
else:
    print("else block")
finally:
    print("finally block")
