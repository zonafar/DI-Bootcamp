####################################
# Exercise 2 : TheIncredibles Family
####################################
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

from Exercise1 import Family

# print(Family)
class TheIncredibles(Family):
    def __init__(self,last_name):
        super().__init__(last_name)
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]
    def use_power(self,name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] > 18:
                    print(f"{member['name']} power is to :  {member['power']}")
                else:
                    raise Exception('You are not over 18 years old')
    def incredible_presentation(self):
        super(TheIncredibles,self).family_presentation()
        for member in self.members:
            print(f"{member['name']} {self.last_name} can {member['power']} ")
    def born(self,**kwargs):
        dictio = {}
        dictio["name"] = kwargs["name"]
        dictio["power"] = kwargs["power"]
        dictio["incredible_name"] = kwargs["incredible_name"]
        # dictio.update({"name" : kwargs["name"]})
        dictio.update({"age" : kwargs["age"]})
        dictio.update({"gender" : kwargs["gender"]})
        dictio.update({"is_child" : kwargs["is_child"]})
        self.members.append(dictio)

print("****** Start *****")
famous_family = TheIncredibles("Holiday")
famous_family.use_power("Michael")
famous_family.incredible_presentation()
famous_family.born(name = "Jack",gender = "Male",is_child = True,age = 2,power = "Unknown_power",incredible_name = "BabyJack")
famous_family.incredible_presentation()
print("****** Fin *****")