# # Challenge 1
# while True:
#     try:
#         numb = int(input("Enter a number : "))
#         length = int(input("Enter a lenght now : "))
#         break
#     except ValueError:
#         print("***** Not a value *** Retry")
#         continue
# multiple = []
# val = numb
# while len(multiple) < length:
#     if numb%val == 0:
#         multiple.append(numb)
#     numb += 1
# print(f"number : {numb} length : {length}")
# print(multiple)

# Challenge 2
# user = "cccccaaarrrbbonnnnn"
user= input("Enter a string : ")
user = list(user)

def concat_list(list):
    string=""
    for i in list:
        string += i
    return string

final = []
for i,elem in enumerate(user):
    cnt= i
    repeat = elem
    duplicate = 0
    stp = 0
    while elem == repeat:
        duplicate += 1
        cnt +=1
        if cnt == len(user):
            break
        else:
            repeat = user[cnt]
    if duplicate  == 1:
        final.append(elem)
print(f"Final string with any duplicate consecutive letters : {concat_list(final)}")
