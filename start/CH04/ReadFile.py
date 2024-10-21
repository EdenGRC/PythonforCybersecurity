#!/usr/bin/env python3
# Sample script that reads from a file
# By Eden

#initail message.
print("Here is someone to hack - ")

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

#Open file for reading.
f = open(dir_path + "/HackMe.txt", "r")

#Read and print file. 
contents = f.readlines()
print(contents)

#Close file.
f.close()