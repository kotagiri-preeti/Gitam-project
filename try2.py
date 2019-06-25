import math
try:
    print(10/0)
    print(math.pow(2,'a'))
except (ZeroDivisionError,TypeError):
    print("exception raised")
finally:
    print("finally block is executed")