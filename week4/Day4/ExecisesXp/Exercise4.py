##########################
###  Exercise 4 : Random
##########################
# Instructions
# 1.Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def get_number(para):
    rd = random.randint(1,100)
    if(rd == para):
        print("Congratulation ! You got it")
    else : 
        print(f"Oops it was not {para} but {rd}")
get_number(50)
