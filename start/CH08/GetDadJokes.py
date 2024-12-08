import requests

def get_dad_jokes(): 
    url = "https://icanhazdadjoke.com"

#Headers Get Requests to APIU
    headers = {
    "Accept": "application/json"
    }

    #Send request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #parse the data JSON response 
        joke_data = response.json()
        #print the dad joke, specific JSON
        print(joke_data['joke'])
    else:
        # Print error code that tells us whats wrong.
        print(f"Failed to retrieve Status code: {response.status_code}")

print(get_dad_jokes())