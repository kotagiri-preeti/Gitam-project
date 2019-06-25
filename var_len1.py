def addition(a,*b):
    print(a)
    for i in b:
        print(i)
addition(10,20,30)

sum=lambda a,b,c:a+b+c
print(sum(10,20,30))