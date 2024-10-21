# example generating responses with a function.
#By Eden

def get_input():
    while True: 
        response = input("Is today a good day? (y/n) ".lower())
        if response in ['y', 'n']:
            return response
        else:
            print("invalid response please print y or n")

def send_message():
    for _ in range(10):
        print("It is a great day, indeed!")

#Get and check response
Response = get_input()

if Response == 'y':
    send_message()
else:
    print("It could be a better day.")