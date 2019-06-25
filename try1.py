try:
    a=10
    b=2
    print(a/b)
    a+c
    print(a+'abc')
except ZeroDivisionError as e:
    print("error raised as:",e)
except TypeError as e:
    print("error raised as:",e)
except:
    print("something went wrong")
else:
    print("this is else block")
finally:
    print("end")
    