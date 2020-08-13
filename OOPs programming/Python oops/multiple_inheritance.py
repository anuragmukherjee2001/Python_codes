class Employee:

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        
    def print_details(self):
        return f"The name is {self.name}, salary is {self.salary} and the role is {self.role}"


class Players:

    num_of_games = 4

    def __init__(self, name, game):
      self.name = name
      self.game = game

    def print_details(self):
        return f"The name of the player is {self.name} and the game is {self.game}"   

class CoolEmployee(Employee, Players):
    
    lang = "C++"

    def print_lang(self):
        print(self.lang)

anurag = Players("Anurag", ["Cricket"])

davison = CoolEmployee("Davison", 56000, "CoolProgrammer")

davison.print_lang()
print(davison.print_details())
