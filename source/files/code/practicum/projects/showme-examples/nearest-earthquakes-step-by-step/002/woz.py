from utils import geocoding

B_X = "\033[1m"
B_Z = "\033[0m"


the_command = input("What do you want to do? ")
if the_command == "hello":
    usertext = input("What is your name? ")
    print("Hello", B_X + usertext + B_Z)

elif the_command == 'geocode':
    userlocation = input("What is your location? ")
    print("OK...geocoding:", userlocation)
    georesult = geocoding.geocode(userlocation)
    print(georesult)
else:
    print("Sorry, I don't know how to respond to", the_command)
