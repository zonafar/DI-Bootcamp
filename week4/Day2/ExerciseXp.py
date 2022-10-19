# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:54:08 2022

@author: ZONA
"""

##########################
### Exercise 1 : Set
##########################
#my_fav_numbers = {1,2,3,4,5,7,6,8,9,10}
#my_fav_numbers.add(18)
#my_fav_numbers.add(22)
#my_fav_numbers.remove(22)
#print(my_fav_numbers)
#friend_fav_numbers = {11,13,15,17,19,21}
#our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#print(our_fav_numbers)

##########################
### Exercise 2: Tuple
##########################
#tupl = (5,8,9)
#tup = list(tupl)
#tup.append(13)
#tupl = tuple(tup)
#temp =  15
#tupl = tupl + (temp,)
#print(tupl)

##########################
### Exercise 3: List
##########################

#basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#basket.insert(0, "Apples")
#basket.clear()
#print(basket)

##########################
### Exercise 4: Floats
##########################
# import numpy as np
# print(np.arange(1,2,0.1))
# lst = []
# for i in np.arange(1.5,5,0.5):
#    lst.append(i)
# print(lst)

##########################
### Exercise 5: For loop
##########################
# I already resolved it 

##########################
### Exercise 6: While loop
##########################
#name = ""
#while name != "zona":
#    name = input("guess my name ")

##########################
### Exercise 7: Favorite fruit
##########################

#favorite = input("Your favorite fruits  to separate the fruits with a single space")
#favorite = "mango orange klm"
#lst = favorite.rsplit(" ")
#print(lst)

##########################
### Exercise 8: Who Ordered A Pizza ?
##########################
# user = ""
# toppings = [];
# while user.lower() != "quit" : 
#     user = input("enter a series of pizza toppings, input ‘quit’ stop asking for toppings.")
#     if user.lower() != "quit":
#         print(f"You add {user} toppings on the pizza")
#         toppings.append(user)
# print("----Lists of toppings -----")
# total = 0
# for i in toppings: 
#     print(i)
#     total += 2.5
# total += 10 
# print(f"total price : {total}")

##########################
### Exercise 9: CinemaX
##########################
# names = ['Oscar','sami','lola','doe']
# for i in names:
#     age = int(input(f"{i}, how old are you ?: "))
#     if age<16 or age>21:
#         names.remove(i)
# print("final list is : {}".format(names))

##########################
### Exercise 11 : Sandwich Orders#2
##########################
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich","Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
print("The deli has run out of pastrani")
i=0
while i<len(sandwich_orders):
    if sandwich_orders[i] == "Pastrami sandwich":
        sandwich_orders.remove(sandwich_orders[i])
    i +=1
print("list without pastrani")
print(sandwich_orders)