##########################
###  🌟 Exercise 2 : Dogs
##########################
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog():
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    def bark(sef):
        return f"{sef.name} goes woof!"
    def jump(sef):
        return f"{sef.name} jumps {sef.height * 2} cm high!"

david_dog = Dog(dog_name="rex",dog_height=50)
print(f"Details : {david_dog.bark()} and {david_dog.jump()}")
sarah_dog = Dog(dog_name="teacup",dog_height=20)
print(f"Details : {sarah_dog.bark()} and {sarah_dog.jump()}")

if (david_dog.height > sarah_dog.height):
    print(f"the bigger dog : {david_dog.name}")
else:
    print(f"the bigger dog : {sarah_dog.name}")
    