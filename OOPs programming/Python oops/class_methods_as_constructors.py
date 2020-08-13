class Employee:

    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        
    def increment(self): 
        self.salary = int(self.salary * self.increase)

    @classmethod
    def from_str(cls, emp_string):
        id, fname, lname, salary, age = emp_string.split("-")
        return cls(id, fname, lname, salary, age)      


anurag = Employee(2050, "Anurag", "Mukherjee",44000, 21)
Jason = Employee(2051, "Json", "Roy", 45000, 22)

davison = Employee.from_str("2055-Davison-Hastings-56000-26")

print(davison.fname)
print(davison.salary)
print(davison.age)

