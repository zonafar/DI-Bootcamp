# #####################
# ### Exercise 1 : Hello World
# #####################
from ast import If


print("Hello word\n"*4)

# #####################
# ### Exercise 2 : Some Math
# #####################

r = (99^3) * 8
print(r)

# #####################
# ### Exercise 3 : What Is The Output ?
# #####################
5 < 3 # False
3 == 3 # True
3 == "3" #Error
"3" > 3 #Error
"Hello" == "hello" # False
# #####################
# ### Exercise 4 : Your Computer Brand
# #####################
computer_brand = "HP"
print(f"I have a {computer_brand} computer")
# #####################
# ### Exercise 5 : Your Information
# #####################

name = "zona"
age = 22
shoe_size = 43
info = "I am {} and have {} years old. I love basket. But to play i need a {} shoe size".format(name,age,shoe_size)
print(info)
# #####################
# ### Exercise 6 : A & B
# #####################
a = 65
b=input("Number")
b = int(b)
if a > b :
    print("Hello world")
# #####################
# ### Exercise 7 : Even or Odd
# #####################
number = int(input("Enter your number"))
if number%2 == 0 :
    print("{} is odd".format(number))
else:
    print("{} is even".format(number))


# #####################
# ###  Exercise 9 : Tall Enough To Ride A Roller Coaster
# #####################
inches = input("Your height inches")
cm = inches * 2.45
if (cm > 145):
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")