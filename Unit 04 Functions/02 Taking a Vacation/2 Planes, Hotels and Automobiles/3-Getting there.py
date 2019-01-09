"""Getting There
You're going to need to take a plane ride to get to your location.

def fruit_color(fruit):
  if fruit == "apple":
    return "red"
  elif fruit == "banana":
    return "yellow"
  elif fruit == "pear":
    return "green"
    
The example above defines the function fruit_color that accepts a string as the argument fruit.
The function returns a string if it knows the color of that fruit.

"""

def hotel_cost(nights):
    return nights*140
    print (nights*140)

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
print (plane_ride_cost('Charlotte'))
