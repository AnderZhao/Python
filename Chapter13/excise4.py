def calculateTotal(coinsCount):
    return 25 * coinsCount[0] + \
           10 * coinsCount[1] + \
           5 * coinsCount[2] + \
           1 * coinsCount[3]

quarters = int(raw_input("How many quarters? "))
dimes = int(raw_input("How many dimes? "))
nickels = int(raw_input("How many nickels? "))
pennies = int(raw_input("How many pennies? "))
cions = [quarters, dimes, nickels, pennies]
print "Total value is: $", calculateTotal(cions) * 0.01
