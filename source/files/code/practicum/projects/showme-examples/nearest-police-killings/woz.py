from utils import settings
from utils.bootstrapping import bootstrap
from utils.wrangling import wrangle
from utils.geocoding import geocode
from utils.feeding import feedme
from utils.telling import tellme
from utils.mapping import mapme
import json

if __name__ == '__main__':
    print("What do you want to do?")
    the_command = input()

    if the_command == 'hello':
        print("What is your name?")
        username = input()
        print("Well hello there", username)

    elif the_command == 'help':
        print("Here are the commands!")

        print("bootstrap")
        print(bootstrap.__doc__)

        print("wrangle")
        print(wrangle.__doc__)

        print("geocode")
        print(geocode.__doc__)

        print("feedme")
        print(feedme.__doc__)

        print("tellme")
        print(tellme.__doc__)

        print("mapme")
        print(mapme.__doc__)





    elif the_command == 'bootstrap':
        print("LET US BOOTSTRAP!")
        bootstrap()

    elif the_command == 'wrangle':
        print("WRANGLE THAT DATA!")
        wrangle()

    elif the_command == 'geocode':
        print("Type in a location to geocode:")
        user_location = input()
        res = geocode(user_location)
        print(json.dumps(res, indent=4))

    elif the_command == 'feedme':
        print("Enter longitude:")
        lng = input()
        print("Enter latitude:")
        lat = input()
        feedme(lng, lat)


    elif the_command == 'tellme':
        print("What is your current location?")
        user_location = input()
        tellme(user_location)


    elif the_command == 'mapme':
        print("What is your current location?")
        user_location = input()
        mapme(user_location)


    else:
        print("Did not recognize command", the_command)
