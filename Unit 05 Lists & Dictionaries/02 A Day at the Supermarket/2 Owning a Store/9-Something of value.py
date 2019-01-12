"""Something of Value
For paperwork and accounting purposes, let's record the total value of your inventory. It's nice to know what we're worth!"""


prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print( "price: %s" % prices[key])
    print( "stock: %s \n" % stock[key])

total = 0


for n in stock:
    total = total + (stock[n] * prices[n])

print (total)
