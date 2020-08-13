class Employee:

    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        
    def increment(self): 
        self.salary = int(self.salary * self.increase)

    @staticmethod
    def isopen(day):
        if day == 'sunday':
          return False
        else:
          return True        


anurag = Employee(2050, "Anurag", "Mukherjee",44000, 21)
Jason = Employee(2051, "Json", "Roy", 45000, 22)

davison = Employee.from_str("2055-Davison-Hastings-56000-26")

print(Employee.isopen('sunday'))
print(Employee.isopen('monday'))
print(davison.isopen('monday'))


