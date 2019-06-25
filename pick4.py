import pickle
class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def display(self):
        print(self.eno,"\t",self.ename)
f=open("manish.txt","wb")
n=int(input("enter no.of employees"))
for i in range(n):
    eno=int(input("enter employee number"))
    ename=input("enter employee name")
    e=Employee(eno,ename)
    pickle.dump(e,f)
f.close()
