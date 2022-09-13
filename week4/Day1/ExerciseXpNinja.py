# #####################
# ### Exercise 1 : Use The Terminal
# #####################

# #####################
# ### Exercise 2 : Alias
# #####################

'''On Windows : 
doskey python=py
'''
# #####################
# ### Exercise 3 : Outputs
# #####################

3 <= 3 < 9
# True
3 == 3 == 3
# True
bool(0)
# False
bool(5 == "5")
# False
bool(4 == 4) == bool("4" == "4")
# True
bool(bool(None))
# False

# #####################
# ### Exercise 4 : How Many Characters In A Sentence ?
# #####################

my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua.  Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
len(my_text)

# #####################
# ### Exercise 5: Longest Word Without A Specific
# #####################

long_sentence = ""
record = "bch"
iswith = True
l_r = len(record)
l_s = len(long_sentence)
while l_r > l_s or iswith == True:
    print(f"\n Higher score : {len(record)}")
    long_sentence = input('long sentence without a "A"')
    if "A".lower() in long_sentence.lower():
        iswith = True
        print(f"There is a A : {l_s}")
    else:
        iswith = False
        l_s= len(long_sentence)
        print(f"You got : {l_s}")