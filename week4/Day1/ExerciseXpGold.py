# #####################
# ### Exercise 1 : Hello World-I Love Python
# #####################

print("Hello world\n" * 4 +"I love python\n" * 4)

# #####################
# ### Exercise 2 : What Is The Season ?
# #####################

month = int(input("what is  month (1 to 12). ?"))

if month in [12,1,2] : 
    print("Winter")                      
elif month in [9,10,11] :
    print("Automn")                      
elif month in [6,7,8] :
    print("Summer")                      
elif month in [3,4,5] :
    print("Spring")       
else : 
    print("Not a month number")               


