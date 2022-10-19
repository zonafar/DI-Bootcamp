# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
# You have 30 minutes to finish this challenge :
try:
    number = int(input("Input: --\t"))
    liste = [n for n in range(1,number) if (number % n == 0 and n != number)]
    if sum(liste) == number:
        print(True)
    else:
        print(False)
except:
    print("Error")