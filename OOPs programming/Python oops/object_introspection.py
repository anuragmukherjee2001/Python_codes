import inspect

class Employee:
    def __init__(self, fname, lname):
      self.fname = fname
      self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set"
        return f"{self.fname}{self.lname}@gmail.com"  

anurag = Employee("Anurag", "Mukherjee")          
davison = Employee("Davison", "Hastings")

print(anurag.print_email)

print(anurag.email)
print(id("this is a string"))
print(id("that is a string"))
print(dir("that is a string"))
print(dir(anurag))
print(type(anurag))
print(inspect.getmembers(anurag))
