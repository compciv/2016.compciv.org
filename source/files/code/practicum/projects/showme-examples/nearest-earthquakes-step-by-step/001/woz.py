B_X = "\033[1m"
B_Z = "\033[0m"


the_command = input("What do you want to do? ")
if the_command == "hello":
    usertext = input("What is your name? ")
    print("Hello", B_X + usertext + B_Z)

elif the_command == 'help':
    print("TODO: help")

elif the_command == 'geocode':
    print("TODO: geocode it")


else:
    print("Sorry, I don't know how to respond to", the_command)