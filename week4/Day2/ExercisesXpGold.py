##########################
### Exercises 1: Concatenate list
##########################
## concatenates two lists together without using the + sign.
# list1=["banana","mango","ice-cream"]
# list2=[1,9,6,7]
# for elem in list2:
#     list1.append(elem)
# print(list1)
##########################
### Exercise 2: Range Of Numbers
##########################
# I already done it before

##########################
### Exercise 3: Check The Index
##########################
# I already done it before

##########################
### Exercise 4: Greatest Number
##########################
# I already done it before

############################
### Exercise 5: The Alphabet
############################

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# for alph in alphabet : 
#     if alph in ['a','e','u','i','o','y'] : 
#         print(f"{alph} is a vowel")
#     else :
#         print(f"{alph} is a consonnant")

############################
### Exercise 6: Words And Letters
############################

# words = []
# while len(words) < 7:
#     user = input("Enter a word in the list")
#     words.append(user)
# letter = input("Enter a letter")
# print(words)
# print(letter)
# for word in words:
#     if letter in word : 
#         print(f"{letter} in index: {word.index(letter)} of {word}")
#     else:
#         print(f"{letter} not in {word}")

############################
### Exercise 7:
############################

# million_number = list(range(1,1000001))
# print(min(million_number))
# print(max(million_number))
# print(sum(million_number))

############################
### Exercise 8 : List And Tuple
############################
# sequ = "34,67,55,33,12,98"
# sequ_list = sequ.rsplit(",")
# sequ_tuple = tuple(sequ_list)
# print(sequ)
# print(sequ_list)
# print(sequ_tuple)

############################
### Exercise 9 : Random Number
############################
import random as rd
get_rand = rd.randrange(1,9)
print(get_rand)
while True:
    user_n = input("input a number from 1 to 9 (including) and press enter (To quit)")
    try:
        user_n = int(user_n)
        if(get_rand == user_n):
            print("Winner")
            break
        else:
            print("Better luck next time")
    except ValueError:
        if(user_n == ""):
            break
        continue 

