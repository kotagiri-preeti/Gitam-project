try:
    a=10
    b=2
    print(a/b)
    a+c
    print(a+'abc')
except ZeroDivisionError as e:  #comment1
    print("error raised as : ",e)
except TypeError as e:
    print("error raised as : ",e)
except: #comment2
    print("something went wrong")
else:   #comment3
    print("this is else block")
finally:    #comment4
    print("end")
     