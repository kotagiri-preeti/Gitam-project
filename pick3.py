import pickle
class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def display(self):
        print(self.eno,"\t",self.ename)
with open("emp.txt","wb") as f:
    e=Employee(100,"abc")
    pickle.dump(e,f)
    print("pickling of employee object is completed")
with open("emp.txt","rb") as f:
    obj=pickle.load(f)
    print("employee information after unpickling")
    obj.display()  