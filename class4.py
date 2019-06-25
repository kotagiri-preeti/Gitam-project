class A:
    def __init__(self):
        print("now in A init")
    def exe(self,a):
        print("hello",a)
class B(A):
    def __init__(self):
        print("now in B init")
        super().__init__()
    def stop(self):
        print("hai")
 
a1=B()
a1.exe("preethi")
a2=A()
del a1
print(help(A))
print(dir(A))
print(id(a1))
