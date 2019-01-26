"""Sending a Letter
Great work!

Now let's write a get_letter_grade function that takes a number score as input and returns a string with the letter grade that that student should receive."""

"""Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.

Inside your function, test score using a chain of if: / elif: / else: statements, like so:

If score is 90 or above: return "A"
Else if score is 80 or above: return "B"
Else if score is 70 or above: return "C"
Else if score is 60 or above: return "D"
Otherwise: return "F"
Finally, test your function!

Print the resulting letter grade with print. Call the get_letter_grade function and pass in get_average(lloyd)."""

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total

def get_average(student):
    homework = average(student["homework"])* 0.1
    quizzes = average(student["quizzes"])* 0.3
    tests = average(student["tests"])* 0.6

    avrg = homework + quizzes + tests
    return avrg

def get_letter_grade(score):
    if score>= 90:
        return 'A'
    elif score>= 80:
        return 'B'
    elif score>= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#get_letter_grade

print (get_letter_grade(get_average(lloyd)))
