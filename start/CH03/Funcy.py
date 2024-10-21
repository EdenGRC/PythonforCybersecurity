#!/usr/bin/env python3
# example workign with Functions
#By Eden 

#This is the functions
def print_me(my_string):
    print(my_string)
    return "it worked!"

def say_hello(num_times):
    for x in range(num_times):
        print("Hello World")


#This is where I call the function.
print_me("This is a function")
result = print_me("This is another function with a return value")
print(result)

say_hello(3)

