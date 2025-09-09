import math
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        raise NotImplementedError("SubClasses must Implement area() method")
    
class Circle(Shape):
    def __init__(self, rad):
        super().__init__("Circle")
        self.rad = rad
    def area(self):
        return f"{(math.pi * self.rad * self.rad):.2f}"
    
class Rectangle(Shape):
    def __init__(self, l,b):
        super().__init__("Circle")
        self.l = l
        self.b = b
    def area(self):
        return f"{(self.l*self.b):.2f}"
s = Circle(7)
print(s.area())

r = Rectangle(4, 5)
print(r.area())
