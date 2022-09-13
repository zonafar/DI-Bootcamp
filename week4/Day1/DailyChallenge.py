import random
string = input("Enter a 10 characters long.")
constructor = ""
if len(string) > 10 :
    print("string to long")
elif len(string) < 10:
    print("string not long enough")
print(f" first character : {string[0]} \n last character : {string[-1]}")
for i in string : 
    constructor += i
    print(constructor)
str_list = list(string)
random.shuffle(str_list)
string = "".join(str_list)
print(f"new string : {string}")