num = int(input("Enter the number of day-old loaves: "))

def bread () : 

    regular  = 3.49
    discount = 0.06

    regular = num * regular
    discount = regular * discount
    total   = regular - discount

    return regular , discount , total

print (bread ()) 