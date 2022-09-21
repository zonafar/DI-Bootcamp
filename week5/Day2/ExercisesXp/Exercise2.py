# #########################################
# # 🌟 Exercice 2 : Chiens
# #########################################
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self,other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*self.weight:
            return f"{self.name} win the fight"
        return f"{other_dog.name} win the fight"

dog1 = Dog("boby",5,30)
dog2 = Dog("rex",6,31)
dog3 = Dog("rickson",7,33)
print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog3.fight(dog1))
print(dog2.fight(dog3))
