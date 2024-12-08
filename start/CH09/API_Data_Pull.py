#the four library
import hashlib
import requests
import secrets
import string

# function that generates a password

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_specieal=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase #adds upper case letters A-Z
    if use_lower: 
        characters += string.ascii_lowercase #adds lower case letters a-z
    if use_digits:
        characters += string.digits #adds digits 0-9
    if use_specieal:
        characters += "!@#$%^&*(){}[]:;<>,.?/`~" #adds special characters
    
    if not characters:
        raise ValueError("No character sets selected for password generator.")
     
    return ''.join(secrets.choice(characters) for _ in range (length))
    
# Function that checks the password with the haveibeenpwned API

def check_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('usf-8')).hexdigest().upper()

    # I am at 30:50 mins






password = generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_specieal=True)
print(f"This is the new password: {password}")