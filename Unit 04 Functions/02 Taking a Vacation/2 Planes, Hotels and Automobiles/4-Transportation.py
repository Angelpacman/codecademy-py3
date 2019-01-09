"""Transportation
You're also going to need a rental car in order for you to get around.

def finish_game(score):
  tickets = 10 * score
  if score >= 10:
    tickets += 50
  elif score >= 7:
    tickets += 20
  return tickets
In the above example, we first give the player 10 tickets for every point that the player scored. Then, we check the value of score multiple times.

First, we check if score is greater than or equal to 10. If it is, we give the player 50 bonus tickets.
If score is just greater than or equal to 7, we give the player 20 bonus tickets.
At the end, we return the total number of tickets earned by the player.
Remember that an elif statement is only checked if all preceding if/elif statements fail.
"""
#Below your existing code, define a function called rental_car_cost with an argument called days.

#Calculate the cost of renting the car:

#Every day you rent the car costs $40.
#if you rent the car for 7 or more days, you get $50 off your total.
#Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
#You cannot get both of the above discounts.
#Return that cost.

#Just like in the example above, this check becomes simpler if you make the 7-day check an if
#statement and the 3-day check an elif statement.

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
