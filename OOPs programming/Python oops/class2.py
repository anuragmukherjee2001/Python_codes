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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good", string)

anurag = Employee("Anurag", 1000, 21, "Programmer")

amit = Employee("Amit", 2000, 23, "Coder")

Rohan = Employee.from_dash("Rohan-4800-22-Sweeper")

print(Rohan.age)
Employee.printgood("Amit")
print(anurag.print_details())