class abc:
    x = 20

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("add:%d"%(self.a+self.b))

    def sub(self):
        pass
    def __del__(self):
        pass

a=abc(10,20)
a.add()
a.sub()
a.b=30 #updating 
del a.b #deleting attribute 'b'
a.b=50  #adding attributes
print(a.b)
#accessing attribites using functions
print(getattr(abc, 'x'))
print(hasattr(abc, 'x'))
print(setattr(abc, 'x',40))
print(abc.x)
delattr(abc,'x')