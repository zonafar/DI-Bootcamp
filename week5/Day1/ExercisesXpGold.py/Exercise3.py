####################################
###  # Exercise 3 : Restaurant Menu Manager
####################################
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.

# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.

class MenuManager():
    def __init__(self):
        self.menu = {
            "name" : ["Soup","Hamburger","Salad","French Fries","Beef bourguignon"], 
            "price": [10,15,18,5,25], 
            "spice_level" : ["B","A","A","C","B"],
            "gluten_index":[False,True,False,False,True]
            }
    def add_item(self,name, price, spice, gluten):
        if name in self.menu["name"]:
            print("Dishe already exist")
        else:
            self.menu["name"].append(name)
            self.menu["price"].append(price)
            self.menu["spice_level"].append(spice)
            self.menu["gluten_index"].append(gluten)
    def update_item(self,name, price, spice, gluten):
        if name in self.menu["name"]:
            idx = self.menu["name"].index(name)
            self.menu["name"][idx] = name
            self.menu["price"][idx] = price
            self.menu["spice_level"][idx] = spice
            self.menu["gluten_index"][idx] = gluten
        else:
            print("the dish is not in the menu.")
    def remove_item(self,name):
        if name in self.menu["name"]:
            idx = self.menu["name"].index(name)
            self.menu["name"].remove(name)
            price = self.menu["price"][idx] 
            self.menu["price"].remove(price) 
            spice = self.menu["spice_level"][idx]
            self.menu["spice_level"].remove(spice) 
            gluten = self.menu["gluten_index"][idx]
            self.menu["gluten_index"].remove(gluten)
        else:
            print("the dish is not in the menu.")
    
        
menu_init = MenuManager()
menu_init.update_item(name = "Salad", price = 20, spice = "B", gluten=True)
print(menu_init.menu)
print()
menu_init.remove_item(name = "Salad")
print(menu_init.menu)


