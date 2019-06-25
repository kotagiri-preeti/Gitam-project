# Python program to demonstrate error if we 
# forget to invoke __init__() of parent. 
class A: 
    a=50
    def __init__(self, n): 
            self.name = n 
class B(A): 
    b=10
    def __init__(self,name,roll): 
            super().__init__(name)
            self.roll = roll 
            self.name=name

object1= B("rahul",13) 
print (object1.name,object1.roll) 
object1.name="abc"
object1.roll=23
print (object1.name,object1.roll) 
print(B.a,B.b)
setattr(B, 'b', 40)
print(B.b)

