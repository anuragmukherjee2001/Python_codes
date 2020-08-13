class Employee:

    def __init__(self, id, fname, lname, salary, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        
    def increment(self): 
        self.salary = int(self.salary * self.increase)          

class Programmer(Employee):
    def __init__(self, id, fname, lname, salary, age, plang, exp):
      super().__init__(id, fname, lname, salary, age)
      self.plang = plang
      self.exp = exp  

    def print_prog(self):
        return f"The name of the programmer is {self.fname} {self.lname} and his salary is {self.salary}"  

anurag = Programmer(2050, "Anurag", "Mukherjee",44000, 21, 'Python', 3)

print(anurag.print_prog())

