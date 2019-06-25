import pickle
class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def display(self):
        print(self.eno,"\t",self.ename)
f=open("manish.txt","rb")
print("employee details")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFError:
        print("all employees completed")
        break
f.close()
