import json
class MenuManager():
    def __init__(self,file):
        with open(file) as f:
            self.menu = json.load(f)

    def add_item(self,name, price):
        dict = {
            "name":name,
            "price":price
        }
        self.menu["items"].append(dict)

    def remove_item(self,name):
        deleted = False
        for i,item in enumerate(self.menu["items"]):
            if (item['name'].upper() == name.upper()):
                del self.menu["items"][i]
                deleted = True
        return deleted

    def save_to_file(self,file,data):
        with open(file,"w") as f:
            json.dump(data,f,indent = 2,sort_keys = True)
            
# file  = "C:/Users/ZONA/3D Objects/Orange DI/DI-Bootcamp/week5/Day4/ExerciseXpGold/restaurant_menu.json"
# obj = MenuManager(file)
# # print(obj.menu['items'])
# print("\n------\tUser menu\t--------")
# for i,item in enumerate(obj.menu['items']):
#     print(f"{i}) {item['name']} {item['price']}")