import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

def make_change(charge, given):
    charge = int(charge*100)
    given = int(given*100)
    change = given - charge
    hundo = fiddies = twenties = tens = fives = ones = quarters = dimes = nickels = pennies = 0
    if change < 0:
        return "You have not given enough."
    if change == 0:
        return 0
    while change > 0:
        if change >= 10000:
            hundo += 1
            change -= 10000
        elif change >= 5000:
            fiddies += 1
            change -= 5000
        elif change >= 2000:
            twenties += 1
            change -= 2000
        elif change >= 1000:
            tens += 1
            change -= 1000
        elif change >= 500:
            fives += 1
            change -= 500
        elif change >= 100:
            ones += 1
            change -= 100
        elif change >= 25:
            quarters += 1
            change -= 25
        elif change >= 10:
            dimes += 1
            change -= 10
        elif change >= 5:
            nickels += 1
            change -= 5
        else:
            pennies += 1 
            change -= 1

    return {"hundos": hundo,
            "fiddies": fiddies, 
            "twenties": twenties, 
            "tens": tens, 
            "fives": fives, 
            "ones": ones,
            "quarters": quarters,
            "dimes": dimes,
            "nickels": nickels,
            "pennies": pennies}

print(make_change(a, b))
