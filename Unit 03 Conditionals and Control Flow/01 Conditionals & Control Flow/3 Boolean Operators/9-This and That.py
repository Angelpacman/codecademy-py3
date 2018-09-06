bool_one = False or not True and True
print(bool_one)


bool_two = False and not True or True
print(bool_two)


bool_three = True and not (False or False)
print(bool_three)


bool_four = not not True or False and not True
print(bool_four)


bool_five = False or not (True and True)
print(bool_five)
