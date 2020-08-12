class Employee:
    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age

anurag = Employee(2050, "Anurag", "Mukherjee",44000, 21)
Jason = Employee(2051, "Json", "Roy", 45000, 22)

print(anurag.fname, Jason.fname)
print(anurag.lname, Jason.lname)
print(anurag.id, Jason.id)
print(anurag.age, Jason.age)
print(anurag.salary, Jason.salary)
print(anurag.age, Jason.age)

