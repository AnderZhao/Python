size = float(raw_input("How big is your gas tank, in liters?"))
percent = float(raw_input("How full is your tank?"))
kmPerLiter = float(raw_input("How many km per liter does your car get?"))
anotherKm = size * percent * 0.01 * 10
print "You can go another", anotherKm, "km"
print "The next gas station is 200 km away"
if anotherKm > 200:
    print "You can wait for the next station."
else:
    print "Get gas now!"
