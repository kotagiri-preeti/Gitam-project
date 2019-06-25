class A: 
    def __init__(self, a,b): 
        self.a = a 
        self.b = b

    def __add__(self,other):
        return(self.a+other.a,self.b+other.b)
    def __gt__(self, other):
        if(self.a>other.a,self.b>other.b):
            return True
        else:
            return false

ob1 = A(2,3) 
ob2 = A(3,4)
print(ob1+ob2)
print(ob1>ob2)












'''
def __gt__(self, other):
    if (self.a + self.b > other.a + other.b):
        return True
    else:
        return False
    
if(ob1>ob2): 
    print("ob1 is greater than ob2") 
else: 
    print("ob2 is greater than ob1") 
'''