class Employee:
    num_of_leaves = 0

    def __init__(self, name, age, salary, role):
      self.name = name
      self.age = age
      self.salary = salary
      self.role = role

    def print_details(self):
        return f"The name is {self.name}, salary is {self.salary}, age is {self.age}, and the role is {self.role}"

    @classmethod
    def print_leaves(cls, newleaves):
        cls.num_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary 

    def __repr__(self):
        return self.print_details()   

    def __str__(self):
        return "This is a string"            

emp1 = Employee("Anurag", 22, 45000, "Programmer")        
emp2 = Employee("Davison", 21, 5000, "Sweeper")

print(emp1 + emp2)
print(emp1 / emp2)

print(emp1)
print(repr(emp1))