class A:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def details(self):
        print("id:",self.id,"name:",self.name)
class B(A):
    def __init__(self,id,name,average):
        self.average=average
        super().__init__(id,name)
    def details(self):
        super().details()
        print("average:",self.average)
a=B(123,"abc",75)
a.details()
