# The four library
import hashlib
import requests
import secrets
import string

# Function that generates a password

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase #adds upper case letters A-Z
    if use_lower: 
        characters += string.ascii_lowercase #adds lower case letters a-z
    if use_digits:
        characters += string.digits #adds digits 0-9
    if use_special:
        characters += "!@#$%^&*(){}[]:;<>,.?/`~" #adds special characters
    
    if not characters:
        raise ValueError("No character sets selected for password generator.")
     
    return ''.join(secrets.choice(characters) for _ in range (length))

# Function that generates the password in with hyphens because I like that format
def generate_password_with_hyphens(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    password_with_hyphens = '-'.join(password[i:i+4] for i in range(0, len(password), 4))
    return password_with_hyphens
    
# Function that checks the password with the haveibeenpwned API

def check_password_pwned(password_with_hyphens):
    sha1_hash = hashlib.sha1(password_with_hyphens.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
   
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code !=200:
        raise ConnectionError(f"Error, unable to connect API status code {response.status_code}")

        #Check that the suffix appears in the response
    breached_hashes = response.text.splitlines()
    for line in breached_hashes:
        hash_suffix, count = line.split(':')
        if suffix == hash_suffix:
            return int(count)
        
    return 0 # Password not found in the database.

# Function to save passwords to a file

def save_password(password, filename="saved_passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}")

# Generate the password

password = generate_password_with_hyphens(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True)
print(f"This is the new password: {password}")

# Checks if password is breached

breaches = check_password_pwned(password)
if breaches > 0:
    print(f"Warning: the generated password has been found in {breaches} breaches, please use another password.")
else:
    print(f"This password has been found in {breaches} breaches, it is unique and can be used safely.")
    save_password(password)