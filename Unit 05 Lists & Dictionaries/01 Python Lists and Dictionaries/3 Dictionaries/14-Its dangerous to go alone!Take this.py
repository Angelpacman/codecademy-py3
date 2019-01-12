"""It's Dangerous to Go Alone! Take This
Let's go over a few last notes about dictionaries

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]
In the example above, we created a dictionary that holds many types of values.
The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.
Finally, we print the letter "c". When we access a value in the dictionary like my_dict["fish"], we have direct access to that value (which happens to be a list). We can access the item at index 0 in the list stored by the key "fish".
"""


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['pocket'].sort()
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['backpack'].sort()
inventory['gold'] = inventory['gold'] +50
