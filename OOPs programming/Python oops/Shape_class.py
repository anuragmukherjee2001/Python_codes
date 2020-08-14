class Rectangle:

    def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth

    def area(self):
        return self.length * self.breadth 

    def peri(self):
        return 2 * (self.length + self.breadth)    


class Square:

    def __init__(self, length):
      self.length = length
      

    def area(self):
        return self.length * self.length 

    def peri(self):
        return 4 * self.length  


rect = Rectangle(22,55)
sq = Square(22)

print(rect.area())
print(sq.area())