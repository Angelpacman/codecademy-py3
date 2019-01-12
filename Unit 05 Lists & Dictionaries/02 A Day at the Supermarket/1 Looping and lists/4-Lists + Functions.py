"""
Lists + Functions
Functions can also take lists as inputs and perform various operations on those lists.

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print small
In the above example, we define a function count_small that has one parameter, numbers.
We initialize a variable total that we can use in the for loop.
For each item n in numbers, if n is less than 10, we increment total.
After the for loop, we return total.
After the function definition, we create an array of numbers called lotto.
We call the count_small function, pass in lotto, and store the returned result in small.
Finally, we print out the returned result, which is 2 since only 4 and 8 are less than 10.
"""
# Write your function below!
def fizz_count(x):
    count = 0
    for i in x:
        if (i == "fizz"):
            count = count  + 1
    return count
    print (count)

#ejemplo de implementacion de la funcion
fizz_count(("robot","toto","fizz", "fizz"))
