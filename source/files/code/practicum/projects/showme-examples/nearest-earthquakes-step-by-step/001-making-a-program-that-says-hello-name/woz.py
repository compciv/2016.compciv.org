B_X = "\033[1m"
B_Z = "\033[0m"


the_command = input("What do you want to do? ")
if the_command == "hello":
    usertext = input("What is your name? ")
    print("Hello", B_X + usertext + B_Z)

elif the_command == 'help':
    print("TODO: help")

elif the_command == 'bootstrap':
    print("TODO: bootstrap stuff")

elif the_command == 'geocode':
    print("TODO: geocode it")

elif the_command == 'wrangle':
    print("TODO: wrangle some data")

elif the_command == 'filtrate':
    print("TODO: filtrate that data")

elif the_command == 'report':
    print("TODO: make a report")

elif the_command == 'publish':
    print("TODO: publish a web report")


else:
    print("Sorry, I don't know how to respond to", the_command)
