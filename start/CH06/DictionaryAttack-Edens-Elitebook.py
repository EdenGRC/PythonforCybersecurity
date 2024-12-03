#Script that performs a dictionary attack against known password hashes.
#Needs a dictionary file. 
#By Eden S.

#Import libraries for hashing.
from passlib.hash import sha512_crypt
#File paths

shadowFile = r"C:\Users\piegu\OneDrive\Documents\GitHub\PythonforCybersecurity\start\CH06\shadow" 
PasswordFile = r"C:\Users\piegu\OneDrive\Documents\GitHub\PythonforCybersecurity\start\CH06\top1000.txt"
CrackedPasswords = r"C:\Users\piegu\OneDrive\Documents\GitHub\PythonforCybersecurity\start\CH06\CrackedPasswords.txt"

#Create a function  to guess our password.

def GuessPassword(ShadowFile, PasswordFile):
    successful_attempts = [] #Lists to store successful username/passwords

    with open(ShadowFile, 'r') as sf, open(PasswordFile, 'r') as pf:
        shadows = sf.readlines()
        passwords = pf.readlines()

        for shadow in shadows:
            #Split once and unpack usernae and password bash.
            parts = shadow.split(':')
            if len(parts) < 2 or '!' in parts[1] or '*' in parts[1]:
                continue #Skip the unwanted lines.

            Username, HashPassword = parts[0], parts[1].strip()
                
            for password in passwords: 
                password = password.strip()

                    #Attempt to verify the password matches the SHA-512 hash. 
                try: 
                    if sha512_crypt.verify(password, HashPassword):
                        successful_attempts.append((Username, password))
                        break 
                except ValueError: 
                    continue #Skip invalid hashes. 
    
    # Write successful passwords found to output file.
    with open(CrackedPasswords, 'w') as of:
        for Username, password in successful_attempts:
            of.write(f"{Username}:{password}\n")             
    
    #Print successful passwords found.
    print("Successful Password Found.")
    for Username, password in successful_attempts:
        print(Username, password)

# Call the function. 
GuessPassword(shadowFile, PasswordFile)

