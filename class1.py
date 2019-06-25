class Employee:
    "Common base class for all employees"
    empCount = 0   
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount():
        print("Total Employee:",Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
emp1 = Employee("Zara", 2000)#"This would create first object of Employee class"
emp2 = Employee("Manni", 5000)#"This would create second object of Employee class"
emp1.displayEmployee()
emp2.displayEmployee()
Employee.displayCount()
