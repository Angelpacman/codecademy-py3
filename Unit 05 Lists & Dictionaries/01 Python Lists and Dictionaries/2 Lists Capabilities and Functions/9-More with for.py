"""More with 'for'
If your list is a jumbled mess, you may need to sort() it.

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
  print animal
First, we create a list called animals with three strings. The strings are not in alphabetical order.
Then, we sort animals into alphabetical order. Note that .sort() modifies the list rather than returning a new list.
Then, for each item in animals, we print that item out as "ant", "bat", "cat" on their own line each."""


start_list = [5, 3, 1, 2, 4]
square_list = []

# for loop number is ambiguous variable

for number in start_list:
    square = number ** 2 # calculate square to add later
    square_list.append(square) # add the calculation
    square_list.sort()
print (square_list) # print sorted version
