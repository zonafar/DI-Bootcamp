# Reverse The Sentence
# Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You




# You have 30 minutes to finish this challenge :
sentence = input("Input :\t")
# sentence = "You have entered a wrong domain"

liste = sentence.split(" ")
liste.reverse()
sentence = ""
for item in liste:
    sentence = sentence + " " + item
print(f"Output : {sentence}")