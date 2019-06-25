from math import *


class Circle:
    def __init__(self,r):
        self.r=r

    def area(self,r):
        return pi*self.r*self.r,pi*r*r

    def perimeter(self):
        return 2*pi*self.r


c=Circle(7)
print(c.area(1))
print(c.perimeter())