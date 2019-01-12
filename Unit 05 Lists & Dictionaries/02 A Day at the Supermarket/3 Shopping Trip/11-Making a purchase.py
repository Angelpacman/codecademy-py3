"""Making a Purchase
Good! Now you're going to need to know how much you’re paying for all of the items on your grocery list.

def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

n = [1, 2, 5, 10, 13]
print sum(n)
In the above example, we first define a function called sum with a parameter numbers.
We initialize the variable total which we will use as our running sum.
For each number in the list, we add that number to the running sum total.
At the end of the function, we return the running sum.
After the function, we create, n, a list of numbers.
Finally, we call the sum(numbers) function with the variable n and print the result.
1.
Define a function compute_bill that takes one argument food as input.

In the function, create a variable total with an initial value of zero.

For each item in the food list, add the price of that item to total.

Finally, return the total.

Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.

"""


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
        total = total + prices[n]
    return total
