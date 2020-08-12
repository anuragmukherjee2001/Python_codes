class Employee:

    increase = 1.5
    num_of_employee = 0

    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        Employee.num_of_employee += 1

    def increment(self): 
        self.salary = self.salary * self.increase


print(Employee.num_of_employee)
anurag = Employee(2050, "Anurag", "Mukherjee",44000, 21)
print(Employee.num_of_employee)
Jason = Employee(2051, "Json", "Roy", 45000, 22)
print(Employee.num_of_employee)

print(anurag.salary)
anurag.increment()
print(anurag.salary)

