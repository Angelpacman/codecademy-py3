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
