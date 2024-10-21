import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file to write to.
f = open(dir_path + "/HackMe.txt", "w") 

#Write to file.
print("hello World")
f.write("What is your name?\n")
f.write("What is your favorite color?\n")
f.write("What is your first pets name?\n")
f.write("What is your mothers maiden name?\n")
f.write("What elementary school did you attend?\n")

#Close file.
f.close()