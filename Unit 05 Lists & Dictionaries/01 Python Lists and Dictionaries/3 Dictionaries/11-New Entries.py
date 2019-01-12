"""
New Entries
Like Lists, Dictionaries are mutable. This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:

dict_name[new_key] = new_value
An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.

The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That's right: you can put lists inside dictionaries!)"""


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print( menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['treta'] = 2.3
menu['treta2'] = 24.3
menu['treta3'] = 22.3


print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)
