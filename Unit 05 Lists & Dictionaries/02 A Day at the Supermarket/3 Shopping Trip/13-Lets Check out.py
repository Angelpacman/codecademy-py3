"""Let's Check Out!
Perfect! You've done a great job with lists and dictionaries in this project. You've practiced:

Using for loops with lists and dictionaries
Writing functions with loops, lists, and dictionaries
Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).
Thanks for shopping at the Codecademy supermarket!"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for n in food:
        if stock[n] > 0:
            total = total + prices[n]
            stock[n] -= 1
        else:
            total = total
    print (total)
    return total
