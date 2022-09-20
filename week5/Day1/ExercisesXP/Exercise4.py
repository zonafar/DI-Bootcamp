##########################
###  # Exercise 4 : Afternoon At The Zoo
##########################
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and self.groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_self.groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo():
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []
        self.groups = {}
    def add_animal(self,new_animal):
        if new_animal in self.animals:
            print("Already in the list")
        else:
            self.animals.append(new_animal)
    def get_animals(self):
        # self.animals.sort()
        print(self.animals)
        for animal in self.animals:
            print(animal)
    def animal_sold(self,sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
        else:
            print("Not in the list")
    def sort_animal(self):
        self.animals.sort()
        for animal in self.animals : 
            isAdd = False
            for key,value in self.groups.items():
                if value: 
                    first_elem = value[0]
                    if first_elem[0] == animal[0]:
                        self.groups[key].append(animal)
                        isAdd = True
            if isAdd == False:
                length = len(self.groups)
                self.groups[length+1] = []
                self.groups[length+1].append(animal)
        return self.groups
    def get_groups(self):
        for group in self.groups.values():
            print(group)

ramat_gan_safari = Zoo("Weogo")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("baboon")
ramat_gan_safari.add_animal("cat")
ramat_gan_safari.add_animal("eel")
ramat_gan_safari.add_animal("cougar")
ramat_gan_safari.add_animal("bear")
ramat_gan_safari.add_animal("ape")
ramat_gan_safari.add_animal("emu")
# 
ramat_gan_safari.get_animals()
print(ramat_gan_safari.sort_animal())
# 
ramat_gan_safari.get_groups()
