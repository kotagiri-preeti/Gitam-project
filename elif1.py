m1=int(input("enter marks1"))
m2=int(input("enter marks2"))
m3=int(input("enter marks3"))
total=(m1+m2+m3)
per=(total/3)
if per>75:
    print("A grade")
elif per>65 and per<75:
    print("b grade")
elif per>45 and per<65:
    print("c grade")
else:
    print("failed")

