"""Practice Makes Perfect
Let's create a few more functions just for good measure.

def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")
The example above is just there to help you remember how functions are structured.

Don't forget the colon at the end of your function definition!
"""
"""1.
First, def a function called cube that takes an argument called number. Don't forget the parentheses and the colon!

Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).

Define a second function called by_three that takes an argument called number.

if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.

Don't forget that if and else statements need a : at the end of that line!
"""

def cube(number):
    raw = number **3
    return raw

def by_three(number):
    if number % 3 == 0:
        number = number **3
        print (number)
        return number
    else:
        print ('n isnt')
        return False
