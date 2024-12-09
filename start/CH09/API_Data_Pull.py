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
    prefix = sha1_hash[:5]
    suffix = sha1_hash[:5]
   
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



#generate the password

password = generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_specieal=True)
print(f"This is the new password: {password}")

# if password is breached
breaches = check_password_pwned(password)
if breaches > 0:
    print(f"Warning: the generated password has been found in {breaches} please use another password.")
else:
    print(f"This password is unique and can be used safely.")


#Things to do

# Create stored passwords like a mini password manager
#Create an input from user about there password to the query the API to see if its compromised
#Emails and utilizes that aspect of api to query if has appeard in any breach.