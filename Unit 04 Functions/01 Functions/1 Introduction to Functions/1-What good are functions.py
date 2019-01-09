"""What Good are Functions?
You might have considered the situation where you would like to reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
"""

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#ahora vamos a hacer la misma funcion pero traducida
def impuesto(la_cuenta):
    #agregar el iva a la cuenta
    la_cuenta = la_cuenta * 1.15
    print("Con impuesto la cuenta tiene un valor de: %f" % la_cuenta)
    return la_cuenta

def propina(la_cuenta):
    #""""vamos a agregar el valor de la propina a la cuenta (12%)"""
    la_cuenta = la_cuenta * 1.12
    print('Con propina la cuenta tiene un valor de: %f' % la_cuenta)
    return la_cuenta

pizza_familiar = 240
pizza_familiar_con_IVA = impuesto(pizza_familiar)
pizza_familiar_con_propina = propina(pizza_familiar_con_IVA)
