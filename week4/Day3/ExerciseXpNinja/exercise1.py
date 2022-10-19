# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
brand = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# Convert it into a list using Python (don’t do it by hand!).
brand_list = brand.split(",")
# Print out a message saying how many manufacturers/companies are in the list.
print(f"There is {len(brand_list)} manufacturers/companies")
# Print the list of manufacturers in reverse/descending order (Z-A).
list_b = brand_list.sort()
brand_list.reverse()
print(brand_list)

# Using loops or list comprehension:
    # Find out how many manufacturers’ names have the letter ‘o’ in them.
letter_o  = len([item for item in brand_list if item.lower().find('o') != -1])
print(f"Number of letters 'o' in the list: {letter_o}")
    # Find out how many manufacturers’ names do not have the letter ‘i’ in them.
letter_i  = len([item for item in brand_list if item.lower().find('i') == -1])
print(print(f"No letter 'i' in the list: {letter_i}"))
# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
duplicate_brand = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Toyota", "Chevrolet"]
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
new = []
y=False
new_string = ""
for it in duplicate_brand:
    y=False
    for itm in new:
        if it == itm:
            y=True
    if y == False:
        new.append(it)
        new_string = new_string + "," + it
print(new_string)
print(f"There is {len(new)} manufacturers/companies")

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
# new = new.reverse()
final = []
for item in new:
    it = item[::-1]
    final.append(it)
final.reverse()
print(final)

