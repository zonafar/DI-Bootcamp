####################################
###  # Exercise 1 : Geometry
####################################
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

class Circle():
    def __init__(self,radius = 1.0):
        self.radius = radius
    def perimeter(self):
        return self.radius * 3.1415 * 2
    def area(self):
        return 3.14 * self.radius**2
    def definition(self):
        print("A circle is a shape consisting of all points in a plane that are at a given distance from a given point, the centre")
mini_circle = Circle()
print(mini_circle.perimeter())
print(mini_circle.area())
print(mini_circle.definition())