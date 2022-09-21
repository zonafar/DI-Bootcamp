# #######################################
# # 🌟 Exercice 3 : Chiens Domestiqués
# #######################################
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

import Exercise2
import random

class PetDog(Exercise2.Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        self.trained = True
        self.bark()
        return self.trained
    def play(self,*args):
        print(f"{args} all play together")
    def do_a_trick(self):
        tricks =  ["does a barrel roll","stands on his back legs","shakes your hand","plays dead"]
        if self.train():
            print(f"{self.name} {random.choice(tricks)}")

print("***** start *****")
dog1 = PetDog("toby",5,30)
dog2 = PetDog("dex",6,31)
dog3 = PetDog("rick",7,33)

dog3.train()
dog3.play("toby","dex","simps")
dog3.do_a_trick()
print("***** end *****")