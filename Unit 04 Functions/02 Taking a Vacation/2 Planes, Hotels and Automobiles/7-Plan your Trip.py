"""Plan Your Trip!
Nice work! Now that you have it all together, let's take a trip.

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of
spending money?
"""
#After your previous code, print out the trip_cost( to "Los Angeles" for 5 days with
#an extra 600 dollars of spending money.

#Don't forget the closing ) after passing in the 3 previous values!


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

def trip_cost(city, days, spending_money):
    notreal = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return notreal

print (trip_cost("Los Angeles", 5, 600))
