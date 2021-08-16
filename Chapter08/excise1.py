number = int(raw_input("Which multiplication table would you like?"))
print "Here's your table:"
for i in range(1, 11):
    print number, "x", i, "=", number * i
