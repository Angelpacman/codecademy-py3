"""Slicing Lists and Strings
You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.

my_list[:2]
# Grabs the first two items
my_list[3:]
# Grabs the fourth through last items
If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included."""


animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:] # From the seventh character to the end
