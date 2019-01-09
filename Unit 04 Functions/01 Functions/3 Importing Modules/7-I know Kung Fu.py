"""I Know Kung Fu
Remember import this from the first exercise in this course?
That was an example of importing a module.
A module is a file that contains definitions—including variables and functions—that
you can use once it is imported."""
#
#   Before we try any fancy importing, let's see what Python already knows about square roots.
#   On line 3 in the editor, ask Python to:

#           print sqrt(25)

#which we would expect to equal five.
#Instead, it throws an error.

# Ask Python to print sqrt(25) on line 3.

from math import *
print(sqrt(25))
