class Employee:

    increase = 1.5

    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        
    def increment(self): 
        self.salary = int(self.salary * self.increase)

    @classmethod
    def change_increment(cls, amount):
        cls.increase = amount    


anurag = Employee(2050, "Anurag", "Mukherjee",44000, 21)
Jason = Employee(2051, "Json", "Roy", 45000, 22)

print(anurag.salary)
Employee.change_increment(3)
anurag.increment()
print(anurag.salary)
# print(anurag.salary)

