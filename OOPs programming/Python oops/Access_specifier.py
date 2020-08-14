# Public Private and protected variables

class Employee:
    num_of_leaves = 0

    _protected = 1
    __private = 200

    def __init__(self, name, age, salary, role):
      self.name = name
      self.age = age
      self.salary = salary
      self.role = role

    def print_details(self):
        return f"The name is {self.name}, salary is {self.salary}, age is {self.age}, and the role is {self.role}"

anurag = Employee("Anurag", 1000, 21, "Programmer")


print(anurag._protected)
print(anurag._Employee__private)
