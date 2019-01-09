"""Review: Built-In Functions
Perfect! Last but not least, let's review the built-in functions you've learned about
in this lesson.

def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2
"""
#First, def a function called distance_from_zero, with one argument (choose any argument
#name you like).

#If the type of the argument is either int or float, the function should return the
#absolute value of the function input.

#Otherwise, the function should return "Nope"



def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        no = abs(num)
        return no
    else:
        return 'Nope'
