# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

user = input("Encrypt (e) or Decrypt (d)").lower()
text = input ("Text: _\t")
shift = int(input ("Shift: _\t"))
# text =  "gafar"
if user == "e":
    cypher_text = ""
    for letter in text:
        if letter.isalpha():
            cypher_text += chr(ord(letter) + shift)
        else: 
            cypher_text += letter
    print("Output:\t",cypher_text)
elif user=="d":
    cypher_text = ""
    for letter in text:
        if letter.isalpha():
            cypher_text += chr(ord(letter) - shift)
        else: 
            cypher_text += letter
    print("Output:\t",cypher_text)
else:
    print("Entry not correct")

