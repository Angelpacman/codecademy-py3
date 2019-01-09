"""
Hey, You Never Know!
You can't expect to only spend money on the plane ride, hotel, and rental car when going on a vacation. There also needs to be room for additional costs like fancy food or souvenirs.
"""
#Modify your trip_cost function definition. Add a third argument, spending_money.

#Modify what the trip_cost function does. Add the variable spending_money to the sum
#that it returns.

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
