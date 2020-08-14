from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def print_area(self):
        return 0

    @abstractmethod
    def print_peri(self):
        return 0    

class Rectangle(Shape):

    type = "Rectangle"
    sides = 4

    def __init__(self):
      self.length = 6
      self.breadth = 4

    def print_area(self):
        return self.length * self.breadth

    def print_peri(self):
        return 2 * (self.length + self.breadth)    

class Square(Shape):

    def __init__(self):
      self.length = 6

    def print_area(self):
        return self.length * self.length  

    def print_peri(self):
        return 4 * self.length    
             


rect1 = Rectangle()  
sq1 = Square()   

print(rect1.print_area())
print(sq1.print_area())
print(sq1.print_peri())
print(rect1.print_peri())