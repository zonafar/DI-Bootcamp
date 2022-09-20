############################################
###### Daily Challenge: Old MacDonald’s Farm
############################################
# Instructions : Old MacDonald’s Farm

# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = {}
    def add_animal(self,animal,quantity = 1):
        isIn = False
        for key,value in self.animals.items():
            isIn = False
            if key == animal:
                old_qty = self.animals[key]
                self.animals[key] = old_qty + quantity
                isIn = True
        if isIn == False:
            self.animals[animal] = quantity
        return self.animals
    def get_info(self):
        print(f"{self.name}'s farm")
        print()
        for key,value in self.animals.items():
            print(f" {key} : {value}")
        print()
        print("\t\tE-I-E-I-0!")
        return ""
    # Expand The Farm
    def get_animal_types(self):
        types = []
        for type in self.animals.keys():
            types.append(type)
        return types
    def get_short_info(self):
        print(f"{self.name}'s farm has : ")
        last_elem = self.get_animal_types()[-1]
        for type in self.get_animal_types():
            if type == last_elem:
                print(f"and {type}")
            else:
                print(type)

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()



# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

