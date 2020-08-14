class Employee:
    def __init__(self, fname, lname):
      self.fname = fname
      self.lname = lname
    #   self.email = f"{self.fname}{self.lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set"
        return f"{self.fname}{self.lname}@gmail.com"  

    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None    

anurag = Employee("Anurag", "Mukherjee")          
davison = Employee("Davison", "Hastings")

print(anurag.print_email)

anurag.fname = "Json"

print(anurag.print_email)


anurag.email = "anurag.davison@gmail.com"

print(anurag.email)

del anurag.email

print(anurag.email)