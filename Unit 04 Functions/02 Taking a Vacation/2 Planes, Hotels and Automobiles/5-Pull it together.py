"""
Pull it Together
Great! Now that you've got your 3 main costs figured out, let's put them together in order to find the total cost of your trip.

def double(n):
  return 2 * n

def triple(p):
  return 3 * p

def add(a, b):
  return double(a) + triple(b)
We define two simple functions, double(n) and triple(p) that return 2 times or 3 times their input. Notice that they have n and p as their arguments

We define a third function, add(a, b) that returns the sum of the previous two functions when called with a and b, respectively. Notice that even though the names of the parameters for add(a, b) are different than the names of the parameters for double(n) and triple(p) we can still pass them into those functions as arguments

"""

#Below your existing code, define a function called trip_cost that takes two parameters, city and days and returns the sum of calling the rental_car_cost(days), hotel_cost(days - 1), and plane_ride_cost(city) functions.

#Notice that we changed the argument of hotel_costs() from nights to days - 1. Since we want trip-cost to only depend on two parameters, we have to convert the variable nights into days. If you are going to be staying somewhere, the number of nights you stay there is one less than the number of days you were there (imagine a weekend trip to visit family, you leave Saturday and return Sunday, so you visit for two days, but only stay for one night).



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

def rental_car_cost(days):
    total = days*40
    if days >= 7:
        tuto = total - 50
        return tuto
    elif days >= 3 and days < 7:
        tato = total - 20
        return tato
    else:
        total = days*40
        return total

def trip_cost(city, days):
    notreal = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
    return notreal
