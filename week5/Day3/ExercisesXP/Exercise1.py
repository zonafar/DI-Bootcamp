# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().

name = input('Your name: ')
print(name)
print(abs(-2))
print(int('65')+22)

# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.
class Doct():
    def __doc__(self):
        print("This is a test about dunder methods")

    def hello():
        '''
        Greatings function
        '''
        pass
doc1 = Doct()
print(doc1.__doc__())
print(doc1.hello().__doc__())
