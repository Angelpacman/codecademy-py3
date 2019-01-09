"""Parameters and Arguments
Let's take another look at the definition of the function square from the previous exercise:


def square(n):


Here, n is a parameter of square. A parameter is a variable that is an input to a function. It says, "Later, when square is used, you'll be able to input any value you want, but for now we'll call that future value n." A function can have any number of parameters.
The values of the parameters passed into a function are known as the arguments. Recall in the previous example, we called:


square(10)


Here, the function square was called with the parameter n set to the argument 10.
Typically, when you call a function, you should pass in the same number of arguments as there are parameters.

To summarize:
    When defining a function, placeholder variables are called parameters.
    When using, or calling, a function, inputs into the function are called arguments.
"""


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print ("%d a la potencia %d es %d." % (base, exponent, result))

power(37,4)  # Add your arguments here!
