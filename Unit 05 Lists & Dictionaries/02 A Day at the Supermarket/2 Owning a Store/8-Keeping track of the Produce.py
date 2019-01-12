"""Keeping Track of the Produce
Now that you have all of your product info, you should print out all of your inventory information.

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
  print "Once: %s" % once[key]
  print "Twice: %s" % twice[key]
In the above example, we create two dictionaries, once and twice, that have the same keys.
Because we know that they have the same keys, we can loop through one dictionary and print values from both once and twice."""

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

for key in prices:
    print ("%s" %key)
    print ("price: %s" %prices[key])
    print ("stock: %s \n" %stock[key])
