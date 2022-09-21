################################
# Exercise 1 : Family
################################
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family():
    def __init__(self,last_name):
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        self.last_name = last_name
    def born(self,**kwargs):
        dictio = {}
        dictio["name"] = kwargs["name"]
        # dictio.update({"name" : kwargs["name"]})
        dictio.update({"age" : kwargs["age"]})
        dictio.update({"gender" : kwargs["gender"]})
        dictio.update({"is_child" : kwargs["is_child"]})
        self.members.append(dictio)
        print("Welcome to the new born and congratulation")
    def is_18(self,name):
        for member in self.members:
            if (member["name"]== name):
                if member["age"] > 18:
                    return True
        return False
    def family_presentation(self):
        for member in self.members:
            print(f"{member['name']} {self.last_name} ")

# # 
# little_family = Family("Fox")
# little_family.born(name = "Sami", age = 3,is_child = True,gender = "Male")
# print(little_family.is_18("Sarah"))
# little_family.family_presentation()
