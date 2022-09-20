####################################
###  # Exercise 2 : Custom List Class
####################################
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
import random
class MyList():
    def __init__(self,list_letters):
        self.letters= list_letters
    def reversed(self):
        self.letters.reverse()
        return self.letters
    def sorted(self):
        self.letters.sort()
        return self.letters


mylist1 = MyList([1,7,3,11,5,15])
print(mylist1.letters)
print(mylist1.reversed())
print(mylist1.sorted())
print()
mylist2 = [ random.randint(0,20) for e in mylist1.letters]
print(mylist2)